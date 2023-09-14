import customtkinter as ctk
from mainFrame.Messages import MMessage, UMessage, SMessage


class MessageContainer(ctk.CTkScrollableFrame):
    last_sender = None
    message_row = 0

    def render_message(self, text, sender):
        self.message_row += 1
        if sender == "":
            MMessage(self, text, self.message_row, self.last_sender == sender)
        elif sender == "server":
            SMessage(self, text, self.message_row)
        else:
            UMessage(self, text, sender, self.message_row, self.last_sender == sender)
        self.last_sender = sender

    def __init__(self, master, **kwargs):
        super().__init__(master, height=600, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.pack(expand=True, fill="both", ipadx=10, ipady=10)
