import customtkinter as ctk


class ChatInput(ctk.CTkFrame):
    def __init__(self, master, on_submit, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        font = ctk.CTkFont(family="sans-serif", size=16)

        self.on_submit = on_submit

        self.input = ctk.CTkEntry(self, placeholder_text="Input your message...", font=font)
        self.input.grid(row=0, column=0, sticky="we", padx=(10, 10))

        button = ctk.CTkButton(self, width=80, fg_color="green", hover_color="dark green", text="send", command=self.submit, font=font)
        button.grid(row=0, column=1, padx=(0, 10))

        self.grid(row=2, column=0, sticky="swe", ipadx=10, ipady=10)

    def submit(self):
        self.on_submit(self.input.get())
        self.input.delete(0, 'end')