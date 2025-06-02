import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        print(f"Recebido: {message}")
        await websocket.send(f"Echo: {message}")

async def main():
    # Aqui, serve() retorna um objeto de servidor dentro de um loop em execução
    async with websockets.serve(echo, 'localhost', 8765):
        print("Servidor WebSocket rodando em ws://localhost:8765")
        # Mantém o servidor ativo para sempre (ou até interrupção manual)
        await asyncio.Future()

if __name__ == "__main__":
    # Cria o event loop, executa “main()” dentro dele e fecha ao final
    asyncio.run(main())
