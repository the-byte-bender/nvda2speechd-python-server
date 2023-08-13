import asyncio
import websockets
import msgpack
from accessible_output2 import outputs

speaker = outputs.auto.Auto()

def parse_message(data):
    try:
        return  msgpack.unpackb(data, raw=False)
    except Exception as e:
        print("Error parsing message:", e)

async def serve(websocket, path):
    async for message in websocket:
        message = parse_message(message)
        if type(message) is  str: 
            if message.lower() == 'cancelspeech':
                speaker.output("", interrupt=True)
        elif type(message) is dict:
            text = message["SpeakText"]
            speaker.output(text, interrupt=False
)

start_server = websockets.serve(serve, "localhost", 3457, ping_timeout = None)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

