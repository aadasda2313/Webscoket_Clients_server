import asyncio
import websockets
import json
connected = set()

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "1234"


array_busy = []
array_free = []
connected_clients = {}


async def check_admin():
    
    pass


async def admin_handler():
    pass



async def send_to_client(ip, message):
    websocket = connected_clients.get(ip)
    if websocket:
        try:
            await websocket.send(message)
            print(f"Sent to {ip}: {message}")
        except Exception as e:
            print(f"Failed to send to {ip}: {e}")
    else:
        print(f"No client with IP {ip} connected.")
        
        
        

async def handler(websocket):
    ip = websocket.remote_address[0]
    connected_clients[ip] = websocket


    


    try:
        async for msg in websocket:
            print(f"Received from {ip}: {msg}")
            response_user_client = '{"btn1": true, "btn2": true, "btn3": false, "btn4": false, "btn5": false, "drive_to": 10}'
            response_esp32 = '{"cmd": move_to, "distance": x}'
            await websocket.send(response_user_client)
            if "START" in msg:
                print("instart")
                
            else:
                #print("intelse")
                data = json.loads(msg)
                print(data)
                btn_id = data.get("button_id")
                if "move_to" in msg:
                    move = data["move_to"]
                    await send_to_client(button_id, response_esp32.replace("x",move))
                    
                    pass
                else:
                    await websocket.send('{"error": "no_distance"}')
            
            
            
            
    except websockets.ConnectionClosed:
        print(f"Disconnected: {ip}")
    finally:
        connected_clients.pop(ip, None)

async def main():
    async with websockets.serve(handler, "192.168.2.100", 6789):
        print(" Echo server running at ws://192.168.2.100:6789")
        await asyncio.Future()  # keep running

asyncio.run(main())

