import sys

import customtkinter as ctk

from IntroFrame import IntroFrame
from mainFrame.MainFrame import MainFrame

ctk.set_appearance_mode("System")

app = ctk.CTk()
app.title("ChaPy")
app.geometry("600x800")

app.iconbitmap(sys.executable)
# app.resizable(False, False)


app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)


def draw_main_frame():
    if connect_data := intro_frame.get_connect_data():
        intro_frame.destroy()
        main_frame = MainFrame(app, connect_data)
        main_frame.grid(row=0, column=0, sticky="nswe")


intro_frame = IntroFrame(app, draw_main_frame)
intro_frame.grid(row=0, column=0)


if __name__ == "__main__":
    app.mainloop()
    sys.exit(0)
