import customtkinter as ctk
from IntroFrame import IntroFrame
from MainFrame import MainFrame

ctk.set_appearance_mode("System")

app = ctk.CTk()
app.title("ChaPy")
app.geometry("600x800")


app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)


def draw_main_frame():
    if connect_data := intro_frame.get_connect_data():
        intro_frame.destroy()
        main_frame = MainFrame(app, connect_data)
        main_frame.place(x=0, y=0, relwidth=1, relheight=1)


intro_frame = IntroFrame(app, draw_main_frame)
intro_frame.grid(row=0, column=0)

app.mainloop()
