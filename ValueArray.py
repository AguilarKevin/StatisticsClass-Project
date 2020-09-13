import ValueSet
import math

class ValueArray(object):

    values = []
    tableFreq = []

    def __init__(self):
        self.values = []
        self.tableFreq = []

    def addValue(self, value):
        self.values.append(value)

    def CreateTable(self):
        self.values.sort()
        
        i = 0
        while i < len(self.values):
            aux = ValueSet(self.values.get(i),0)
        
            for j in self.values:
                if aux.Mark == k:
                    aux.incrementFreq()
                    i+=1

            self.tableFreq.add(aux)

        return self.tableFreq

    def CalcularModa(self):
        modaIndex = 0

        i = 0
        while i < len(self.tableFreq):
            if self.tableFreq[modaIndex].Freq < self.tableFreq[i].Freq:
                modaIndex = i

        return self.tableFreq[modaIndex].Mark


    def CalcularMedia(self):
        
        aux = 0
        for i in self.values:
            aux += i
    
        return aux/len(values)

    def CalcularMediana(self):
        return self.values[len(self.values)/2]

    def CalcularVarianza(self):
        acMedia = 0
        acMedia2 = 0

        for i in self.values:
            acMedia = acMedia + i
            acMedia2 = acMedia2 + i * i

        n = len(self.values)
        
        return (acMedia2 / (n-1) - (acMedia * acMedia) / (n * (n-1)))

    def CalcularDesviacionEstandar(self):
        return math.sqrt(self.CalcularVarianza())