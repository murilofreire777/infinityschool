from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
socketio = SocketIO(app, async_mode='eventlet')

# Mapeia username -> sid
connected_users = {}

# Jogador aguardando (para emparelhamento)
waiting_player = None

# Armazena estado de cada partida
# games[room] = {
#    'players': (player1, player2),
#    'board': [''] * 9,
#    'turn': player1,
#    'symbols': {player1: 'X', player2: 'O'}
# }
games = {}


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    # Não faz nada imediatamente ao conectar
    pass


@socketio.on('disconnect')
def handle_disconnect():
    sid = request.sid
    # Encontrar qual usuário se desconectou
    user_to_remove = None
    for user, user_sid in connected_users.items():
        if user_sid == sid:
            user_to_remove = user
            break

    if not user_to_remove:
        return

    del connected_users[user_to_remove]

    global waiting_player
    # Se ele estava esperando, remove
    if waiting_player == user_to_remove:
        waiting_player = None

    # Se estava em jogo, notificar oponente e encerrar a partida
    for room, game in list(games.items()):
        if user_to_remove in game['players']:
            player1, player2 = game['players']
            opponent = player2 if player1 == user_to_remove else player1
            opp_sid = connected_users.get(opponent)

            if opp_sid:
                emit('opponent_left', {}, room=opp_sid)
                # Retornar oponente ao lobby
                join_room('lobby', sid=opp_sid)
                emit('returned_lobby', {}, room=opp_sid)

            # Remover ambos da sala e apagar o jogo
            leave_room(room, sid=sid)
            if opp_sid:
                leave_room(room, sid=opp_sid)
            del games[room]
            break


@socketio.on('join_lobby')
def handle_join_lobby(data):
    """
    data = {'username': 'Alice'}
    """
    username = data.get('username', 'Anônimo')
    connected_users[username] = request.sid

    # Entra no lobby
    join_room('lobby')
    emit('lobby_joined', {}, room=request.sid)


@socketio.on('find_match')
def handle_find_match(data):
    """
    data = {'username': 'Alice'}
    """
    global waiting_player
    username = data.get('username')
    sid = request.sid

    if waiting_player is None:
        # Ninguém esperando, esse usuário agora aguarda
        waiting_player = username
        emit('waiting', {}, room=sid)
    else:
        if waiting_player == username:
            # Mesmo usuário clicou duas vezes, ignora
            return

        player1 = waiting_player
        player2 = username
        sid1 = connected_users.get(player1)
        sid2 = sid

        # Cria nome único para a sala de jogo
        room_name = f"game_{uuid.uuid4().hex[:8]}"

        # Inicializa estado do jogo
        games[room_name] = {
            'players': (player1, player2),
            'board': [''] * 9,
            'turn': player1,
            'symbols': {player1: 'X', player2: 'O'}
        }

        # Limpa o jogador aguardando
        waiting_player = None

        # Move player1 do lobby para a sala de jogo
        if sid1:
            leave_room('lobby', sid=sid1)
            join_room(room_name, sid=sid1)
        # Move player2 do lobby para a sala de jogo
        leave_room('lobby', sid=sid2)
        join_room(room_name, sid=sid2)

        # Envia evento de início de jogo para player1
        start_data1 = {
            'room': room_name,
            'symbol': 'X',
            'opponent': player2,
            'board': games[room_name]['board'],
            'your_turn': True
        }
        # E para player2
        start_data2 = {
            'room': room_name,
            'symbol': 'O',
            'opponent': player1,
            'board': games[room_name]['board'],
            'your_turn': False
        }
        if sid1:
            emit('start_game', start_data1, room=sid1)
        emit('start_game', start_data2, room=sid2)


@socketio.on('make_move')
def handle_make_move(data):
    """
    data = {'username': 'Alice', 'room': 'game_abcd1234', 'index': 4}
    """
    username = data.get('username')
    room = data.get('room')
    index = data.get('index')

    game = games.get(room)
    if not game or game['turn'] != username:
        return

    board = game['board']
    if index < 0 or index >= 9 or board[index] != '':
        return

    symbol = game['symbols'][username]
    board[index] = symbol

    # Verifica vencedor ou empate
    winner = check_winner(board)
    if winner:
        player1, player2 = game['players']
        opponent = player2 if player1 == username else player1
        sid_winner = connected_users.get(username)
        sid_loser = connected_users.get(opponent)

        if sid_winner:
            emit('game_over', {'result': 'win', 'board': board}, room=sid_winner)
        if sid_loser:
            emit('game_over', {'result': 'lose', 'board': board}, room=sid_loser)

        cleanup_game(room)
        return
    elif '' not in board:
        # Empate
        for player in game['players']:
            sid_p = connected_users.get(player)
            if sid_p:
                emit('game_over', {'result': 'draw', 'board': board}, room=sid_p)
        cleanup_game(room)
        return
    else:
        # Troca turno
        player1, player2 = game['players']
        next_turn = player2 if username == player1 else player1
        game['turn'] = next_turn

        # Envia atualização de tabuleiro para ambos
        for player in game['players']:
            sid_p = connected_users.get(player)
            if sid_p:
                emit('board_update', {
                    'board': board,
                    'your_turn': (player == next_turn)
                }, room=sid_p)


def check_winner(board):
    """Retorna True se houver vencedor no tabuleiro."""
    win_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]
    for (a, b, c) in win_positions:
        if board[a] != '' and board[a] == board[b] == board[c]:
            return True
    return False


def cleanup_game(room):
    """Finaliza o jogo, derruba a sala e retorna ambos ao lobby."""
    game = games.get(room)
    if not game:
        return

    player1, player2 = game['players']
    sid1 = connected_users.get(player1)
    sid2 = connected_users.get(player2)

    # Remove ambos da sala de jogo e coloca no lobby
    if sid1:
        leave_room(room, sid=sid1)
        join_room('lobby', sid=sid1)
        emit('returned_lobby', {}, room=sid1)
    if sid2:
        leave_room(room, sid=sid2)
        join_room('lobby', sid=sid2)
        emit('returned_lobby', {}, room=sid2)

    # Remove o jogo
    del games[room]


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
