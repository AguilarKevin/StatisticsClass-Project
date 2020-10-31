from tkinter import *
import calc.binomial as binom

class FrameTab2(Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        self.container = LabelFrame(self, text = 'Distribucion binomial')
        self.container.grid(row = 0, column = 0, padx = 20, pady = 20)

        self.n_label = Label(self.container)
        self.n_label["text"] = ("n:")
        self.n_label.grid(row = 0, column = 0, padx = 8, pady = 16)

        self.input_n = Entry(self.container)
        self.input_n.grid(row = 0, column = 1)

        self.r_label = Label(self.container)
        self.r_label["text"] = ("r:")
        self.r_label.grid(row = 1, column = 0, padx = 8, pady = 16)

        self.input_r = Entry(self.container)
        self.input_r.grid(row = 1, column = 1)

        self.p_label = Label(self.container)
        self.p_label["text"] = ("p:")
        self.p_label.grid(row = 2, column = 0, padx = 8, pady = 16)

        self.input_p = Entry(self.container)
        self.input_p.grid(row = 2, column = 1)

        self.calc_btn = Button(self.container, text = "calcular", command = self.calc)
        self.calc_btn.grid(row = 3, column = 0 )

        self.clear_btn = Button(self.container, text = "limpiar", command = self.clear_Entries)
        self.clear_btn.grid(row = 3, column = 1 )


    #handles onClick event for calc_btn
    def calc(self):
        if len(self.input_n.get()) > 0 and len(self.input_p.get()) > 0 and len(self.input_r.get()) > 0:
            n, r, p, = float(self.input_n.get()), float(self.input_r.get()), float(self.input_p.get())
            if p > 1:
                Message.showinfo(title = "Error", message = "p no puede ser mayor a 1")
            else:
                Message.showinfo(title = "Resultado", message = "la probabilidad es:"+ str(binom.calc_binom(n, r, p,)))
        else:
            Message.showinfo(title = "Error", message = "rellene todos los campos")

    def clear_Entries(self):
        self.input_n.delete(0,END)
        self.input_r.delete(0,END)
        self.input_p.delete(0,END)