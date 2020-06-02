import asyncio
import websockets
import json
import time
import random

async def hello(websocket, path):
    while True:
        initial_data_to_send = {
            'textbox_values': [random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100), random.randint(1,100)],
            'graph_data_points': [random.randint(1,100),random.randint(1,100)]
        }

        await websocket.send(json.dumps(initial_data_to_send))

        print(initial_data_to_send)
        time.sleep(0.03)

start_server = websockets.serve(hello, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()