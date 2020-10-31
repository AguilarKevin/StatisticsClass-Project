from tkinter import ttk, END, messagebox, CENTER

class FrameTab1(ttk.Frame):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight = 1)

        self.container = ttk.LabelFrame(self, text = 'medidas de dispersion y desviacion estandar')
        self.container.grid(row = 0,column = 0, ipadx = 55, ipady = 35, sticky = "n, s, w, e ", padx = 5, pady = 5)

        self.container_val = ttk.LabelFrame(self.container, text = 'valores')
        self.container_val.grid(row = 0,column = 0, ipadx = 55, ipady = 35, sticky = "n, s, w", padx = 5, pady = 5)

        self.container2 = ttk.LabelFrame(self, text = 'tabla de frecuencia')
        self.container2.grid(row = 1,column = 0, ipadx = 55, ipady = 35, sticky = "n, s, e, w ", padx = 5, pady = 5)

        self.freqTable = ttk.Treeview(self.container2, height = 10, columns = 2)
        self.freqTable.heading('#0', text = "intervalo", anchor = CENTER)
        self.freqTable.heading('#1', text = "Frequencia", anchor = CENTER)
        self.freqTable.grid(row = 0,column = 0, ipadx = 55, ipady = 35, sticky = "N, S", padx = 5, pady =5)



