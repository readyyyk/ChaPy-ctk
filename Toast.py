import customtkinter as ctk


class Toast(ctk.CTkFrame):
    def __init__(self, master, text, **kwargs):
        super().__init__(master, border_color="#22c55e", fg_color="#14532d", border_width=2, width=300, height=28, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.toast_content = ctk.CTkLabel(self, text=text)
        self.toast_content.grid(row=0, column=0, padx=20, pady=10)

        self.place(relx=.987, rely=.989, anchor="se")
        self.after(5000, self.destroy)
