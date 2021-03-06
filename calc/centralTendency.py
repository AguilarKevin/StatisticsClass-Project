import math
from calc.FrequencyTable import FrequencyTable

class CentralTendency(object):

    def __init__(self):
        self.__NumIntr = 0
        self.__MinValue = 0
        self.__MaxValue = 0
        self.__values = []
        self.__table = None

    def calc(self, numIntervals):
        self.__NumIntr = numIntervals
        self.__values.sort()
        self.__MinValue, self.__MaxValue = self.__values[0], self.__values[-1]

        self.__table = FrequencyTable(self.__MinValue, self.__MaxValue, math.ceil(self.amplitude()),\
             self.__values, self.__NumIntr )

        return "moda= " + str(self.mode()) + "\nmedia= " + str(self.arithmeticMean()) + "\nmediana= "\
            + str(self.median()) + "\nvarianza= "+ str(self.variance()) +"\ndesviacion estandar= "\
                + str(self.standardDeviation())+ "\n\nrango= " + str(self.range()) +\
                     "\namplitud= " + str(math.ceil(self.amplitude()))

    def getTable(self):
        return self.__table.getIntervals()

    def add(self, value):
        self.__values.append(value)
    
    def range(self):
        return ( self.__MaxValue - self.__MinValue)

    def amplitude(self):
        return ( self.range() / self.__NumIntr )

    def mode(self):
        aux = mode = 0
        
        for i in self.__values:
            if aux != i:
                aux = i
                if self.__values.count(aux) > self.__values.count(mode) :
                    mode = aux
        
        return mode

    def arithmeticMean(self):
        aux = 0
        for i in self.__values:
            aux += i

        return aux/len(self.__values)

    def median(self):
        return self.__values[int(len(self.__values)/2)]

    def variance(self):
        acMedia = acMedia2 = 0

        for i in self.__values:
            acMedia = acMedia + i
            acMedia2 = acMedia2 + i * i

        n = len(self.__values)

        return (acMedia2 / (n-1) - (acMedia * acMedia) / (n * (n-1)))

    def standardDeviation(self):
        return math.sqrt(self.variance())
