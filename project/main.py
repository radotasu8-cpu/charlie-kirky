import asyncio
import websockets

clients = set()

async def handler(websocket):
    print("Client connected:", websocket.remote_address)
    clients.add(websocket)

    try:
        async for message in websocket:
            # print("Broadcasting:", message)

            dead = set()
            for client in clients:
                try:
                    await client.send(message)
                except Exception:
                    dead.add(client)

            clients.difference_update(dead)

    except Exception as e:
        print("Handler error:", e)

    finally:
        clients.discard(websocket)
        print("Client disconnected:", websocket.remote_address)

async def main():
    async with websockets.serve(handler, "localhost", 5000):
        await asyncio.Future()

asyncio.run(main())
