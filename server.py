import asyncio
import websockets
import json
connected = set()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"


array_busy = []
array_free = []



async def check_admin():
    
    pass


async def admin_handler():
    pass





async def handler(websocket):
    connected.add(websocket)
    
    is_admin = False

    try:
        async for msg in websocket:
            #print(f" Received: {msg}")
            #data = json.loads(msg)
            print(msg)
            print(f" From: {websocket.remote_address}")
            #await websocket.send(f"Echo from server: {msg}")
            response = '{"btn1": true,"btn2": true,"btn3":false,"btn4":true,"btn5":true,"drive_to":10, "age": 30, "city": "New York"}'
            await websocket.send(response)
            print(websocket)

        ''' if msg.startswith("LOGIN"):
                parts = msg.strip().split()
                print(parts)
                print(len(parts))
                if len(parts) == 3:
                    username, password = parts[1], parts[2]
                    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
                        is_admin = True
                        await websocket.send("LOGIN_SUCCESS")
                        print(" Admin logged in.")
                    else:
                        await websocket.send("LOGIN_FAILED")
                        print(" Invalid login.")
                else:
                    await websocket.send("LOGIN_USAGE: LOGIN <username> <password>")'''
           # else:
                # Normal echo message
            #await websocket.send(f"Echo from server: {msg}")
                

    except websockets.ConnectionClosed:
        print(f" Disconnected: {websocket.remote_address}")
    finally:
        connected.discard(websocket)

async def main():
    async with websockets.serve(handler, "192.168.2.100", 6789):
        print(" Echo server running at ws://192.168.2.100:6789")
        await asyncio.Future()  # keep running

asyncio.run(main())
