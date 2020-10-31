from tkinter import ttk, END, messagebox, IntVar, Text
import calc.binomial as binom

class FrameTab2(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_rowconfigure(0, weight = 1)
        
        self.container = ttk.LabelFrame(self, text = 'Distribucion binomial')
        self.container.grid(row = 0, column = 0, ipadx = 30, ipady = 35, sticky = "N, S", padx = 7, pady = 20)

        self.n_label = ttk.Label(self.container)
        self.n_label["text"] = ("n:")
        self.n_label.grid(row = 0, column = 0, padx = 8, pady = 8)

        self.input_n = ttk.Entry(self.container, width = 7)
        self.input_n.grid(row = 0, column = 1)

        self.p_label = ttk.Label(self.container)
        self.p_label["text"] = ("p:")
        self.p_label.grid(row = 1, column = 0, padx = 8, pady = 8)
        
        self.input_p = ttk.Entry(self.container, width = 7)
        self.input_p.grid(row = 1, column = 1)

        self.selection = IntVar()

        self.R1 = ttk.Radiobutton(self.container, text="P( X >=", variable=self.selection, value=1, command = self.switch)
        self.R1.grid(row = 3, column = 0, padx = 8, pady = 8)

        self.input_r1 = ttk.Entry(self.container, width = 7)
        self.input_r1.grid(row = 3, column = 1,)

        self.r1_label = ttk.Label(self.container)
        self.r1_label["text"] = (")")
        self.r1_label.grid(row = 3, column = 2)

        self.R2 = ttk.Radiobutton(self.container, text="P( X <=", variable=self.selection, value=2, command = self.switch)
        self.R2.grid(row = 4, column = 0, padx = 8, pady = 8)

        self.input_r2 = ttk.Entry(self.container, width = 7)
        self.input_r2.grid(row = 4, column = 1)

        self.r2_label = ttk.Label(self.container)
        self.r2_label["text"] = (")")
        self.r2_label.grid(row = 4, column = 2)

        self.R3 = ttk.Radiobutton(self.container, text="P( X =", variable=self.selection, value=3, command = self.switch)
        self.R3.grid(row = 5, column = 0, padx = 8, pady = 8)

        self.input_r3 = ttk.Entry(self.container, width = 7)
        self.input_r3.grid(row = 5, column = 1)

        self.r3_label = ttk.Label(self.container)
        self.r3_label["text"] = (")")
        self.r3_label.grid(row = 5, column = 2)

        self.calc_btn = ttk.Button(self.container, text = "calcular", command = self.calc)
        self.calc_btn["state"] = "disabled"
        self.calc_btn.grid(row = 7, column = 1, padx = 5, pady = 16)

        self.clear_btn = ttk.Button(self.container, text = "limpiar", command = self.clear_Entries)
        self.clear_btn.grid(row = 7, column = 2, padx = 5, pady = 16 )

        #answer text area
        self.container2 = ttk.LabelFrame(self, text = 'Respuestas')
        self.container2.grid(row = 0, column = 1, ipadx = 55, ipady = 35, sticky = "N, S", padx = 7, pady = 20)

        self.answerTextArea = Text(self.container2, width = 45)
        self.answerTextArea.pack(side = 'left')
        #grid(column = 0, row = 0, columnspan = 1, padx = 16, pady = 20)
        
        self.scrollbar = ttk.Scrollbar(self.container2)
        self.scrollbar.pack(side = 'right', fill = "y", expand = False)

        self.answerTextArea.config( yscrollcommand = self.scrollbar.set )
        self.scrollbar.config( command = self.answerTextArea.yview )


    #handles onClick event for calc_btn
    def calc(self):
        print(self.selection.get())

        if self.validateEntries():
            n, p, = int(self.input_n.get()), float(self.input_p.get())

            rx, ri = 0,0
            if self.selection.get() == 1: 
                #p(x >= r)
                rx, ri = int(self.input_r1.get()), n
            elif self.selection.get() == 2: 
                #p(x <= r)
                rx, ri = 0, int(self.input_r2.get())
            elif self.selection.get() == 3: 
                #p(x = r)
                rx, ri = int(self.input_r3.get()), int(self.input_r3.get())

            print(rx)
            print(ri)

            distBinom = binom.calc_binom(n, rx, ri, p, self.selection.get())
            math_expec = binom.math_expec(n, p)
            self.answerTextArea.insert(END, "Distribucion binomial = "+ str(distBinom))
            self.answerTextArea.insert(END, "\nEsperanza Matematica = "+ str(math_expec) + "\n\n")
        

    def clear_Entries(self):
        self.input_n.delete(0,END)
        self.input_p.delete(0,END)
        self.input_r1delete(0,END)
        self.input_r2delete(0,END)
        self.input_r3delete(0,END)

    def switch(self):
        self.enable_btnCalc()
        
        if self.selection == 1:
            self.input_r2delete(0,END)
            self.input_r3delete(0,END)
        elif self.selection == 2:
            self.input_r1delete(0,END)
            self.input_r3delete(0,END)
        elif self.selection == 3:
            self.input_r1delete(0,END)
            self.input_r2delete(0,END)

    def enable_btnCalc(self):
        if self.calc_btn["state"] == "disabled":
            self.calc_btn["state"] = "normal"

    def rangeIsEmpty(self, i):
        if i == 1:
            return len(self.input_r1.get()) == 0
        elif i == 2: 
            return len(self.input_r2.get()) == 0
        elif i == 3:
            return len(self.input_r3.get()) == 0
    

    def validateEntries(self):
        if len(self.input_n.get()) > 0 and len(self.input_p.get()) > 0:
            if self.rangeIsEmpty(self.selection.get()):
                ttk.messagebox.showinfo(title = "Error", message = "ingrese el rango") 
            else:
                if float(self.input_p.get()) > 1:
                    ttk.messagebox.showinfo(title = "Error", message = "p no puede ser mayor a 1")
                else:
                    return True
        else:
            ttk.messagebox.showinfo(title = "Error", message = "rellene todos los campos")
        
        return False

