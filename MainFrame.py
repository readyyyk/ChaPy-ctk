from typing import List, Dict
import customtkinter as ctk
from threading import Thread
from functools import reduce
import websocket

from Toast import Toast
from messages import MMessage, UMessage


class ChatInfo(ctk.CTkFrame):
    user_list = []

    def add_user(self, name: str):
        delitmer = ", "
        self.user_list.append(name)
        self.user_list_label.configure(text="Users: "+reduce(lambda acc, el: acc + delitmer + el, self.user_list, "")[len(delitmer):])

    def __init__(self, master, chat_id, name, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)

        chat_label = ctk.CTkLabel(self, text=chat_id, font=("sans-serif", 36), text_color="blue")
        chat_label.grid(row=0, column=0, padx=(20, 0))

        name_label = ctk.CTkLabel(self, text=f" - {name}", font=("sans-serif", 32), text_color="#4477CE")
        name_label.grid(row=0, column=1, padx=(0, 20))

        self.user_list_label = ctk.CTkLabel(self, font=("sans-serif", 20), text_color="#8CABFF")
        self.add_user("Me")
        self.user_list_label.grid(row=0, column=2, padx=(10, 20), sticky='e')

        self.grid(row=0, column=0, sticky="we", ipady=10)


class MainFrame(ctk.CTkFrame):
    last_sender = None
    message_row = 0

    def render_message(self, text, sender):
        self.message_row += 1
        if sender == "":
            MMessage(self, text, self.message_row, self.last_sender == sender)
        else:
            UMessage(self, text, sender, self.message_row, self.last_sender == sender)
        self.last_sender = sender

    def __init__(self, master, connect_data, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(0, weight=1)

        self.chat_id = connect_data["chat_id"]
        self.ws_link = connect_data["ws_link"]
        self.name = connect_data["name"]

        # websocket.enableTrace(True)

        self.ws = websocket.WebSocketApp(
            url=self.ws_link,
            on_open=lambda ws: Toast(self, text=f"Successfully connected to chat -{self.chat_id}- as -{self.name}- ✅"),
            on_message=lambda ws, data: print(data),
            on_error=lambda _, a: print(a)
        )

        self.ws_thread = Thread(target=self.ws.run_forever)
        self.ws_thread.start()

        ChatInfo(self, self.chat_id, self.name)

        self.render_message("sadsda as mlkdmkl asdmlk asdmkl adslkm", "zxc")
        self.render_message("mlkdmkl asdmlk asd mk asdmkl adslkm sadsda as ", "")
        self.render_message("asdmkl", "")
