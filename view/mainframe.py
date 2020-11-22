import tkinter as tk
from tkinter import ttk

from view.FrameTab1 import FrameTab1
from view.FrameTab2 import FrameTab2
from view.FrameTab3 import FrameTab3

class Application(ttk.Frame):

    def __init__(self, window):
        super().__init__(window)
        window.title("Proyecto de estadistica")
        window.geometry("800x550")
        window.resizable(0,0)

        self.tabParent = ttk.Notebook(window)
        self.tab1 = FrameTab1(self.tabParent)
        self.tab2 = FrameTab2(self.tabParent)
        self.tab3 = FrameTab3(self.tabParent)

        self.tabParent.add(self.tab1, text = "Asignacion 1")
        self.tabParent.add(self.tab2, text = "Asignacion 2")
        self.tabParent.add(self.tab3, text = "Asignacion 3")
        self.tabParent.pack(expand = 1, fill = 'both')

        self.tabParent.select(self.tab3)
