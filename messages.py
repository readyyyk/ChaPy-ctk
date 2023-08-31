import requests
from io import BytesIO
import customtkinter as ctk
from PIL import Image, ImageOps, ImageDraw

from _consts import AVATAR_API_URL


def get_logo(sender: str):
    im = Image.open(BytesIO(requests.get(AVATAR_API_URL + f"/picsum/{sender}").content))
    mask = Image.new('L', im.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + im.size, fill=255)
    output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)
    return output


class Message(ctk.CTkFrame):
    row = 0
    text = ""
    sender = ""
    same_sender = False

    def render(self, **kwargs):
        self.grid(
            row=self.row, column=0,
            ipadx=16, ipady=8,
            padx=10, pady=(3 if self.same_sender else 10, 0),
            **kwargs
        )

    def __init__(self, master, text, sender, row, same_sender=False, **kwargs):
        super().__init__(master, **kwargs)
        self.row = row
        self.text = text
        self.sender = sender
        self.same_sender = same_sender

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1 if sender == "" else 0)


class UMessage(Message):
    def __init__(self, master, text, sender, row, same_sender=False, **kwargs):
        super().__init__(master, text, sender, row, same_sender, fg_color="#35155D", **kwargs)

        im = get_logo(sender)

        logo = ctk.CTkImage(light_image=im,
                            dark_image=im,
                            size=(40, 40))

        logo_label = ctk.CTkLabel(self, text="", image=logo)
        logo_label.grid(row=0, column=0, padx=(10, 8))

        text_label = ctk.CTkLabel(self, text=text)
        text_label.grid(row=0, column=1)

        self.render(sticky="w")


class MMessage(Message):
    def __init__(self, master, text, row, same_sender=False, **kwargs):
        super().__init__(master, text, "", row, same_sender, **kwargs)

        text_label = ctk.CTkLabel(self, text=text)
        text_label.grid(row=0, column=0)

        self.render(sticky="e")
