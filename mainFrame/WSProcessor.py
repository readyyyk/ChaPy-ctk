import json
from threading import Thread
import websocket
import atexit
from mainFrame.Toast import Toast

from mainFrame.encoding import AESCipher


class WSProcessor:
    ws = None
    name = None
    ws_link = None
    encoder: AESCipher
    ws_thread = None

    def send_message(self, text):
        data_json = json.dumps({
            "event": "message",
            "data": json.dumps({
                "sender": self.name,
                "text": text,
            })
        }, separators=(',', ':'))
        data, iv = self.encoder.encrypt(data_json)

        self.ws.send(json.dumps({"data": data.decode("utf-8"), "iv": iv}))

    def process_ws_message(self, _, data_json: str):
        encoded_data = json.loads(data_json)
        decoded: str = self.encoder.decrypt(encoded_data["data"], encoded_data["iv"]).decode("utf-8")
        ev_data = json.loads(decoded)
        print(data_json)
        match ev_data["event"]:
            case "connection":
                msg_data = json.loads(ev_data["data"])
                self.render_message(f"{msg_data['name']} {msg_data['detail']}", "server")

                if msg_data["detail"] == "connected" and msg_data["name"] != self.name:
                    self.add_user(msg_data['name'])
                elif msg_data["detail"] == "disconnected":
                    self.remove_user(msg_data['name'])

            case "message":
                msg_data = json.loads(ev_data["data"])
                self.render_message(msg_data["text"], msg_data["sender"] if "sender" in msg_data else "")

    def __init__(self, master, connect_data, render_message, add_user, remove_user):
        self.add_user = add_user
        self.encoder = AESCipher(connect_data["key"])
        self.remove_user = remove_user
        self.render_message = render_message

        self.name = connect_data["name"]

        websocket.enableTrace(True)

        self.ws = websocket.WebSocketApp(
            url=connect_data["ws_link"],
            on_open=lambda ws: Toast(master, text=f"Successfully connected to chat -{connect_data['chat_id']}- as -{connect_data['name']}- ✅"),
            on_message=self.process_ws_message,
            on_error=lambda _, a: print(a)
        )

        self.ws_thread = Thread(target=self.ws.run_forever, daemon=True)

        atexit.register(self.ws.close)

        self.ws_thread.start()
