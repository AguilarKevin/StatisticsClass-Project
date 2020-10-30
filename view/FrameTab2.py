from tkinter import ttk
from calc.binomial import calc_binom

class FrameTab2(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title = ttk.Label(self)
        self.title["text"] = ("Distribucion binomial")
        self.title.pack()

        self.container = ttk.Frame(self)
        self.container.pack()

        self.n_label = ttk.Label(self.container)
        self.n_label["text"] = ("n")
        self.n_label.grid(row = 0, column = 0, padx = 8, pady = 16)

        self.input_n = ttk.Entry(self.container)
        self.input_n.grid(row = 0, column = 1)

        self.p_label = ttk.Label(self.container)
        self.p_label["text"] = ("p")
        self.p_label.grid(row = 0, column = 2, padx = 8, pady = 16)

        self.input_p = ttk.Entry(self.container)
        self.input_p.grid(row = 0, column = 3)

        self.x_label = ttk.Label(self.container)
        self.x_label["text"] = ("x")
        self.x_label.grid(row = 0, column = 4, padx = 8, pady = 16)

        self.input_x = ttk.Entry(self.container)
        self.input_x.grid(row = 0, column = 5)

        self.calc_btn = ttk.Button(self.container, text = "calcular", command = calc_binom(0,0,0))
        self.calc_btn.grid(row = 1, column = 0 )

        