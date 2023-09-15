import customtkinter as ctk

from mainFrame.ChatInfo import ChatInfo
from mainFrame.ChatInput import ChatInput
from mainFrame.WSProcessor import WSProcessor
from mainFrame.MessageContainer import MessageContainer


class MainFrame(ctk.CTkFrame):
    ws = None
    name = None
    chat_id = None
    ws_link = None

    def __init__(self, master, connect_data, **kwargs):
        super().__init__(master, **kwargs)

        # self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure(0, weight=1)

        chat_info = ChatInfo(self, connect_data["chat_id"], connect_data["name"])

        msg_container = MessageContainer(self)
        ws_p = WSProcessor(master, connect_data, msg_container.render_message, chat_info.add_users, chat_info.remove_user)

        ChatInput(self, ws_p.send_message)
