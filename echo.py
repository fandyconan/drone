# Importing the relevant libraries
import websockets
import asyncio

PORT = 7890
connected_clients = set()

print("Server listening on Port " + str(PORT))

async def broadcast(message):
    for client in connected_clients:
        await client.send(message)

async def echo(websocket, path):
    print("A client just connected")
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            print("Received message from client: " + message)
            # await websocket.send("Pong: " + message)
            await broadcast(message)
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        connected_clients.remove(websocket)




start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()