# Importing the relevant libraries
import websockets
import asyncio

# The main function that will handle connection and communication 
# with the server
async def listen():
    url = "ws://127.0.0.1:7890"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send a greeting message
        
        # Stay alive forever, listening to incoming msgs
        while True:
            await ws.send(input("Text something:"))
            msg = await ws.recv()
            print(msg)

# Start the connection

asyncio.get_event_loop().run_until_complete(listen())
asyncio.get_event_loop().run_forever()