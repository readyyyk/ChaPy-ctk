from threading import Thread
from functools import reduce
import customtkinter as ctk
import requests

from _consts import SERVER_URL


class ChatInfo(ctk.CTkFrame):
    user_list = []

    def remove_user(self, name: str):
        self.user_list.remove(name)
        self.render_user_list()

    def add_users(self, names: list[str]):
        self.user_list = self.user_list + names
        self.render_user_list()

    def render_user_list(self):
        delitmer = ", "
        self.user_list_label.configure(
            text="Users: " + reduce(lambda acc, el: acc + delitmer + el, self.user_list, "")[len(delitmer):])

    def __init__(self, master, chat_id, name, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)

        chat_label = ctk.CTkLabel(self, text=chat_id, font=("sans-serif", 36), text_color="blue")
        chat_label.grid(row=0, column=0, padx=(20, 0))

        name_label = ctk.CTkLabel(self, text=f" - {name}", font=("sans-serif", 32), text_color="#4477CE")
        name_label.grid(row=0, column=1, padx=(0, 20))

        self.user_list_label = ctk.CTkLabel(self, text="", font=("sans-serif", 20), text_color="#8CABFF")

        self.user_list_label.grid(row=0, column=2, padx=(10, 20), sticky='e')

        # self.grid(row=0, column=0, sticky="nwe", ipady=10)
        self.pack(expand=True, fill="x", ipady=10, anchor="n")
