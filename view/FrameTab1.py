from tkinter import ttk


class FrameTab1(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = ttk.Label(self)
        self.title["text"] = ("varianza y desviacion estandar")
        self.title.pack()

