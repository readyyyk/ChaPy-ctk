from threading import Thread

import customtkinter as ctk
import requests

from _consts import SERVER_URL


class IntroFrame(ctk.CTkFrame):
    name = None
    chat_id = None
    ws_link = None
    fetch_thread = None
    is_first_render = True

    def fetch(self, chat_id, name):
        res = requests.get(SERVER_URL + f"/{chat_id}/connect?name={name}")
        if "message" in res.json():
            self.errors.configure(text=res.json()["message"], bg_color="#7f1d1d")
            return

        self.chat_id = chat_id
        self.name = name
        self.ws_link = res.json()["wsLink"]
        self.callback()

    def submit(self):
        chat_id = self.chat_entry.get()
        name = self.name_entry.get()

        if self.is_first_render:
            self.is_first_render = False
        self.errors.grid(row=3, column=0, padx=20, pady=(0, 20), columnspan=2, sticky="ew")
        self.errors.configure(text="Loading...", bg_color="#2563eb")

        if not chat_id:
            self.errors.configure(text="Enter chat ID!", bg_color="#7f1d1d")
            return
        if not name:
            self.errors.configure(text="Enter name!", bg_color="#7f1d1d")
            return

        self.fetch_thread = Thread(target=self.fetch, args=(chat_id, name), daemon=True)
        self.fetch_thread.start()

    def get_connect_data(self):
        return {
            "ws_link": self.ws_link,
            "chat_id": self.chat_id,
            "name": self.name,
        }

    def __init__(self, master, callback, **kwargs):
        super().__init__(master, **kwargs)
        self.callback = callback

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # chat id
        self.chat_label = ctk.CTkLabel(self, text="Chat ID: ")
        self.chat_label.grid(row=0, column=0, padx=(20, 0), pady=(20, 0))

        self.chat_entry = ctk.CTkEntry(self, placeholder_text="ABCDE")
        self.chat_entry.grid(row=0, column=1, padx=(0, 20), pady=(20, 0))

        # name
        self.name_label = ctk.CTkLabel(self, text="Name: ")
        self.name_label.grid(row=1, column=0, padx=(20, 0), pady=(15, 0))

        self.name_entry = ctk.CTkEntry(self, placeholder_text="Vasya")
        self.name_entry.grid(row=1, column=1, padx=(0, 20), pady=(15, 0))

        # submit
        self.btn = ctk.CTkButton(self, text="Submit", fg_color="green", hover_color="dark green", width=100, command=self.submit)
        self.btn.grid(row=2, column=0, columnspan=2, padx=(20, 20), pady=(20, 20))

        self.errors = ctk.CTkLabel(self, text="", bg_color="#7f1d1d")
