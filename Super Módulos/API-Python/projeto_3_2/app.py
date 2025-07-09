# app.py
import asyncio
from flask import Flask, render_template, request
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
# Usa eventlet como backend assíncrono
socketio = SocketIO(app, async_mode='eventlet')

# Lista fixa (poderia vir de DB) de salas disponíveis
CHAT_ROOMS = ['sala1', 'sala2', 'sala3']

@app.route('/')
def index():
    """
    Renderiza o HTML principal. O cliente deve escolher um nome de usuário
    e então se conecta via Socket.IO, entra automaticamente no 'lobby'.
    """
    return render_template('index.html', rooms=CHAT_ROOMS)


@socketio.on('connect')
def handle_connect():
    """
    Quando o cliente se conecta, não sabemos ainda qual é o nome dele
    (será enviado depois pelo cliente). No entanto, podemos colocar
    o socket na sala 'lobby' imediatamente. A notificação de 'novo membro'
    no lobby acontecerá quando o cliente enviar o próprio nome via evento 'join_lobby'.
    """
    join_room('lobby')
    # Podemos opcionalmente emitir lista de salas atuais para esse cliente
    emit('rooms_list', {'rooms': CHAT_ROOMS}, room=request.sid)


@socketio.on('disconnect')
def handle_disconnect():
    """
    Quando o cliente desconecta, precisamos notificar as salas em que ele estava.
    Idealmente o cliente diria em qual sala estava; como simplificação, informaremos
    a todos na lobby que o usuário saiu (caso tenhamos guardado o nome dele na sessão).
    """
    username = request.args.get('username')  # Vem do query string, se foi passada
    # Esse emit no lobby é apenas ilustrativo; normalmente removeríamos usuário de rooms.
    if username:
        send(f"{username} desconectou.", room='lobby')


@socketio.on('join_lobby')
def handle_join_lobby(data):
    """
    Dados esperados: {'username': 'Alice'}
    Cliente ingressa no lobby (caso não esteja). Todos no lobby são notificados.
    """
    username = data.get('username', 'Anônimo')
    # Armazena o nome na sessão do socket (para referência futura)
    request.environ['username'] = username

    # Caso o usuário já estivesse em outra sala, deixamos explicitamente:
    for room in CHAT_ROOMS + ['lobby']:
        if room in socketio.server.manager.rooms.get('/', {}).get(request.sid, set()):
            leave_room(room)

    # Agora, ingresa no lobby
    join_room('lobby')
    send(f"{username} entrou no Lobby.", room='lobby')

    # Envia lista de salas ao cliente (por precaução)
    emit('rooms_list', {'rooms': CHAT_ROOMS}, room=request.sid)


@socketio.on('join_room')
def handle_join_room(data):
    """
    Dados esperados: {'username': 'Alice', 'room': 'sala1'}
    Cliente solicita entrar em “room”. Deve sair do lobby (ou de qualquer outra sala)
    antes de ingressar.
    """
    username = data.get('username', 'Anônimo')
    room = data.get('room')
    if room not in CHAT_ROOMS:
        emit('error_message', {'msg': f"A sala '{room}' não existe."}, room=request.sid)
        return

    # Sai de todas as salas conhecidas (incluindo lobby e outras salas)
    for r in CHAT_ROOMS + ['lobby']:
        if r in socketio.server.manager.rooms.get('/', {}).get(request.sid, set()):
            leave_room(r)

    # Agora ingresa na sala escolhida
    join_room(room)
    send(f"{username} entrou na sala {room}.", room=room)


@socketio.on('leave_room')
def handle_leave_room(data):
    username = data.get('username', 'Anônimo')
    room = data.get('room')
    if room == 'lobby':
        leave_room('lobby')
        send(f"{username} saiu do Lobby.", room='lobby')
        return
    if room not in CHAT_ROOMS:
        emit('error_message', {'msg': f"A sala '{room}' não existe."}, room=request.sid)
        return
    leave_room(room)
    send(f"{username} saiu da sala {room}.", room=room)
    join_room('lobby')
    send(f"{username} voltou ao Lobby.", room='lobby')

@socketio.on('send_message')
def handle_send_message(data):
    """
    Dados esperados: {'username': 'Alice', 'room': 'sala1', 'message': 'Oi pessoal!'}
    O cliente informa para qual sala mandar a mensagem. Se estiver em 'lobby',
    room='lobby'. Caso contrário, room='salaX'.
    """
    username = data.get('username', 'Anônimo')
    room = data.get('room', 'lobby')
    message = data.get('message', '')

    # Envia para todas as pessoas na mesma “room”
    send(f"{username}: {message}", room=room)


if __name__ == '__main__':
    # Nota: usar eventlet ou gevent para produção; aqui apenas ilustramos
    socketio.run(app, host='0.0.0.0', port=5000)