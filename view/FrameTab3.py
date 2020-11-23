from tkinter import ttk, END, messagebox, IntVar, Text, LabelFrame, StringVar, HORIZONTAL, Canvas, SUNKEN
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from calc.confidence_interval import ConfidenceInterval
import scipy.stats as st
import numpy as np

class FrameTab3(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.container = ttk.LabelFrame(self, text = 'Intervalos de Confianza')
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid(row = 0, column = 0, padx= 10, pady = 10, ipadx = 10, ipady = 10)

        self.containerEntries = LabelFrame(self.container, text = "Datos")
        self.containerEntries.grid(row = 0,column = 0,  sticky = "n, s, w", ipady = 10, padx= 10, pady = 10)

        self.graph = ttk.LabelFrame(self.container, text = 'Grafico')
        self.graph.grid(row = 0,column = 1,  sticky = "n, s, e", columnspan = 2)

        self.containerResults = LabelFrame(self.graph, text = "Resultados")
        self.containerResults.grid(row = 0,column = 0,  sticky = "n, s, e", columnspan = 2)

        self.ci_lbl = ttk.Label(self.containerResults, text = "CI para la media:")
        self.ci_lbl.grid(row = 0, column = 0)

        self.x1Entry = ttk.Entry(self.containerResults)
        self.x1Entry.grid(row = 0,column = 1, pady = 8 )

        self.ci_lbl = ttk.Label(self.containerResults, text = "< µ <")
        self.ci_lbl.grid(row = 0, column = 2)

        self.x2Entry = ttk.Entry(self.containerResults)
        self.x2Entry.grid(row = 0,column = 3, pady = 8 )

        self.medianLabel = ttk.Label(self.containerEntries, text = "Media ( x̄ )")
        self.medianLabel.grid(row = 0, column = 0, pady = 8, columnspan = 2)

        self.medianEntry = ttk.Entry(self.containerEntries)
        self.medianEntry.grid(row = 1,column = 0, pady = 8 , columnspan = 2)

        self.standarDeviationLabel = ttk.Label(self.containerEntries, text = "Desviación Estándar(σ)")
        self.standarDeviationLabel.grid(row = 2, column = 0, pady = 8, columnspan = 2)

        self.standarDeviationEntry = ttk.Entry(self.containerEntries)
        self.standarDeviationEntry.grid(row = 3,column = 0, pady = 8, columnspan = 2 )

        self.n_Label = ttk.Label(self.containerEntries, text = "Tamaño de Muestra (n)")
        self.n_Label.grid(row = 4, column = 0, pady = 8, columnspan = 2)

        self.n_Entry = ttk.Entry(self.containerEntries)
        self.n_Entry.grid(row = 5,column = 0, pady = 8, columnspan = 2 )

        self.confidenceLabel = ttk.Label(self.containerEntries, text = "Nivel de Confianza (%)")
        self.confidenceLabel.grid(row = 6, column = 0, pady = 8, padx = 25)

        self.OptionList = ["","90", "91", "92", "93" , "94" , "95" , "96" , "97" , "98" , "99"]
        self.variable = StringVar(self)
        self.variable.set(self.OptionList[0])

        self.confidenceEntry = ttk.OptionMenu(self.containerEntries, self.variable, *self.OptionList)
        self.confidenceEntry.grid(row = 6,column = 1, pady = 8)

        ttk.Separator(self.containerEntries,orient= HORIZONTAL).grid(row=7, columnspan=2, sticky = "ew", padx = 20)

        self.containerBtn = ttk.Frame(self.containerEntries)
        self.containerBtn.grid(row = 8)

        self.calcBtn = ttk.Button(self.containerBtn, text = "calcular", command = self.calc)
        self.calcBtn.grid(row = 0, column = 0, pady = 8, padx = 10)

        self.calcBtn = ttk.Button(self.containerBtn, text = "Limpiar", command = self.clear)
        self.calcBtn.grid(row = 0, column = 1, pady = 8)


    def calc(self):
        X_, sd, percSelect, n = float(self.medianEntry.get()), float(self.standarDeviationEntry.get()),\
            int(self.OptionList.index(self.variable.get())), int(self.n_Entry.get())

        x1, x2 = ConfidenceInterval.calc(percSelect, n, X_, sd)
        self.x1Entry.delete(0,END)
        self.x1Entry.insert(0,"{:.3f}".format(x1))

        self.x2Entry.delete(0,END)
        self.x2Entry.insert(0,"{:.3f}".format(x2))

        z_x1, z_x2 = ConfidenceInterval.calcZValues(95)
        self.addTable(z_x1,z_x2)

    def clear(self):
        self.canvas.delete("all")

    def addTable(self, z_x1, z_x2):
        fig = Figure(figsize = (4, 4),
                    dpi = 80)

        mu, sigma = 0, 1 # media y desvio estandar

        normal = st.norm(mu, sigma)
        x = np.linspace(normal.ppf(0.01),
                normal.ppf(0.99), 100)
        fp = normal.pdf(x)
        plt = fig.add_subplot(111).plot(x, fp)


        f = np.linspace(normal.ppf(z_x1),
                normal.ppf(z_x2), 100)
        fp = normal.pdf(f)

        y1 = np.sin(2 * np.pi * x)
        plt = fig.add_subplot(111).fill_between(f, 0,fp , facecolor='orange', alpha=0.5)

        canvas = FigureCanvasTkAgg(fig, master = self.graph)
        canvas.draw()
        canvas.get_tk_widget().grid(row = 1, column = 0, sticky = "n, s, e, w")
