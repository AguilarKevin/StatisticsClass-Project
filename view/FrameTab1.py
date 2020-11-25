from tkinter import ttk, END, messagebox, CENTER, Text, LabelFrame
from calc.centralTendency import CentralTendency

class FrameTab1(ttk.Frame):

    __centralTendencyObj = CentralTendency()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)

        self.container = LabelFrame(self, text = 'medidas de tendencia central y Medidas de dispersion')
        self.container.grid(row = 0, column = 0,sticky = "w,e,s,n", padx = 5, ipadx = 5)

        #Entries
        self.containerEntries = ttk.LabelFrame(self.container, text = 'Datos')
        self.containerEntries.grid(row = 2, column = 0, rowspan = 1, columnspan = 3, sticky = "e,w", ipadx = 10)

        self.NumIntervLbl = ttk.Label(self.containerEntries, text = "Numero de intervalos:")
        self.NumIntervLbl.grid(row = 0, column = 0)

        self.NumInterv = ttk.Entry(self.containerEntries, width = 15)
        self.NumInterv.grid(row = 0, column = 1, pady = 5)

        self.ValueLbl = ttk.Label(self.containerEntries, text = "valor:")
        self.ValueLbl.grid(row = 1, column =0, padx =10)

        self.Value = ttk.Entry(self.containerEntries, width = 30)
        self.Value.bind('<Return>', self.enterEvent)
        self.Value.grid(row = 1, column = 1, columnspan = 2, padx =10)

        self.btnAggInterv = ttk.Button(self.containerEntries, text = "Agregar", command = self.addValue)
        self.btnAggInterv.grid(row = 1, column = 3, padx =10)

        self.btnCalc = ttk.Button(self.containerEntries, text = "Calcular", command = self.calc)
        self.btnCalc.grid(row = 1, column = 4, padx =10)

        #TextArea values
        self.container_val = ttk.LabelFrame(self.container, text = 'valores')
        self.container_val.grid(row = 0, column = 0, rowspan = 2, sticky = "sw,nw,n,s,w", ipadx = 5)

        self.valuesTxt = Text(self.container_val, width = 25)
        self.valuesTxt.grid(row = 0, sticky = "sw,nw,n,s,w", padx = 5)
        self.valuesTxt["state"] = "disabled"

        self.scrollbar = ttk.Scrollbar(self.container_val)
        self.scrollbar.grid(row = 0, sticky = "e, n, s")

        self.valuesTxt.config( yscrollcommand = self.scrollbar.set )
        self.scrollbar.config( command = self.valuesTxt.yview )

        #frequence table
        self.containerTable = ttk.LabelFrame(self.container, text = 'tabla de frecuencia')
        self.containerTable.grid(row = 0, column = 1, columnspan = 2, sticky = "n, s, e, w")

        self.freqTable = ttk.Treeview(self.containerTable, height = 10, columns =('#1', '#2', '#3', '#4', '#5', '#6'))
        self.freqTable['show'] = 'headings'
        self.freqTable.heading('#1', text = "intervalos", anchor = CENTER)
        self.freqTable.heading('#2', text = "M", anchor = CENTER)
        self.freqTable.heading('#3', text = "f", anchor = CENTER)
        self.freqTable.heading('#4', text = "F", anchor = CENTER)
        self.freqTable.heading('#5', text = "Fr", anchor = CENTER)
        self.freqTable.heading('#6', text = "F%", anchor = CENTER)

        self.freqTable.column("#1", width = 100)
        self.freqTable.column("#2", width = 70)
        self.freqTable.column("#3", width = 70)
        self.freqTable.column("#4", width = 70)
        self.freqTable.column("#5", width = 120)
        self.freqTable.column("#6", width = 120)

        self.freqTable.grid(row = 0, column = 0, sticky = "n, e, w, s")

        #result container
        self.containerResult = ttk.LabelFrame(self.container, text = 'Resultados')
        self.containerResult.grid(row = 1, column = 1, sticky = "n,s,e,w")
        self.ResultTxt = Text(self.containerResult, height = 10, width = 67)
        self.ResultTxt.grid(row = 0, sticky = "w, n, s, e")
        self.ResultTxt["state"] = "disabled"

        self.scrollbar2 = ttk.Scrollbar(self.containerResult)
        self.scrollbar2.grid(row = 0, sticky = "e, n, s")

        self.ResultTxt.config( yscrollcommand = self.scrollbar2.set )
        self.scrollbar2.config( command = self.ResultTxt.yview )


    def enterEvent(self,event):
        self.addValue()


    def addValue(self):
        value = self.Value.get()
        self.__centralTendencyObj.add( int( value ) )
        self.valuesTxt["state"] = "normal"
        self.valuesTxt.insert(END, str(value + ",\n"))
        self.valuesTxt["state"] = "disabled"

    def calc(self):
        if len(self.NumInterv.get()) == 0:
            messagebox.showinfo(title = "Error", message = "Ingrese el numero de intervalos")
        else:
            numIntervals = int(self.NumInterv.get())
            if numIntervals < 1:
                messagebox.showinfo(title = "Error", message = "El numero de intervalos no puede ser 0")
            else:
                self.ResultTxt["state"] = "normal"
                self.ResultTxt.insert(END, self.__centralTendencyObj.calc( numIntervals ))
                self.ResultTxt["state"] = "disabled"
                self.createTable()

    def createTable(self):
        intervals = self.__centralTendencyObj.getTable()
        for i in intervals:
            self.freqTable.insert('', 0,text = "", values = i.get())