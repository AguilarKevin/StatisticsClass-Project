from tkinter import ttk, END, messagebox, IntVar, Text, LabelFrame
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)

class FrameTab3(ttk.Frame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.container = ttk.LabelFrame(self, text = 'Intervalos de Confianza')
        self.container.grid_rowconfigure(0, weight = 1)
        self.container.grid(row = 0, column = 0, sticky = "n,s,w,e")

        self.containerEntries = LabelFrame(self.container, text = "Datos")

        self.containerEntries.grid(row = 0,column = 0,  sticky = "n, s, w", ipady = 10, ipadx = 10, pady = 10)

        self.graph = ttk.LabelFrame(self.container, text = 'Grafico')
        self.graph.grid(row = 0,column = 1,  sticky = "n, s, e", columnspan = 2)

        self.medianLabel = ttk.Label(self.containerEntries, text = "x̄")
        self.medianLabel.grid(row = 0, column = 0, pady = 8)

        self.medianEntry = ttk.Entry(self.containerEntries)
        self.medianEntry.grid(row = 0,column = 1, pady = 8 )

        self.standarDeviationLabel = ttk.Label(self.containerEntries, text = "S")
        self.standarDeviationLabel.grid(row = 1, column = 0, pady = 8)

        self.standarDeviationEntry = ttk.Entry(self.containerEntries)
        self.standarDeviationEntry.grid(row = 1,column = 1, pady = 8 )

        self.n_Label = ttk.Label(self.containerEntries, text = "n")
        self.n_Label.grid(row = 2, column = 0, pady = 8)

        self.n_Entry = ttk.Entry(self.containerEntries)
        self.n_Entry.grid(row = 2,column = 1, pady = 8 )

        self.confidenceLabel = ttk.Label(self.containerEntries, text = "confianza")
        self.confidenceLabel.grid(row = 3, column = 0, pady = 8)

        self.confidenceEntry = ttk.Entry(self.containerEntries)
        self.confidenceEntry.grid(row = 3,column = 1, pady = 8 )

        self.plot(self.graph)

# plot function is created for
# plotting the graph in
# tkinter window
    def plot(self, root):

    # the figure that will contain the plot
        fig = Figure(figsize = (5, 5),
                    dpi = 80)

    # adding the subplot
        plot1 = fig.add_subplot(111)

    # plotting the graph
    # creating the Tkinter canvas
    # containing the Matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master = root)
        canvas.draw()

    # placing the canvas on the Tkinter window
        canvas.get_tk_widget().grid( row = 0)


    # placing the toolbar on the Tkinter window
        canvas.get_tk_widget().grid( row = 0)
