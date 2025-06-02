import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Olá servidor!")
        response = await websocket.recv()
        print(f"Resposta: {response}")

if __name__ == "__main__":
    asyncio.run(hello())