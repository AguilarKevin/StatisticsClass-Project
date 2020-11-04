class intervalo(object):

    def __init__(self, Xmin, Xmax):
        self.__Xmin = Xmin
        self.__Xmax = Xmax
        self.__freq = 0
        self.__freqAcum = 0
        self.__freqRel = 0
        self.__freqPerc = 0
        self.__classMark = 0

    def get(self):
        return str(self.__Xmin)+ "-" + str(self.__Xmax) + " " + str(self.__classMark)  + " " + str(self.__freq)\
             + " " + str(self.__freqAcum) + " " + str(self.__freqRel) + " " + str(self.__freqPerc)  

    def getXmin(self):
        return self.__Xmin

    def getXmax(self):
        return self.__Xmax

    def setFreq(self, value):
        self.__freq = value
    
    def getFreq(self):
        return self.__freq

    def setFreqAcum(self, value):
        self.__freqAcum = value
    
    def getFreqAcum(self):
        return self.__freqAcum

    def setFreqRel(self, value):
        self.__freqRel = value
    
    def getFreqRel(self):
        return self.__freqRel

    def setFreqPerc(self, value):
        self.__freqPerc = value
    
    def getFreqPerc(self):
        return self.__freq

    def setClassMark(self, value):
        self.__classMark = value

    def getClassMark(self):
        return self.__classMark

class CentralTendency(object):

    def __init__(self):
        self.__size = 0

        self.__NumIntr = 0
        self.__MinValue = 0
        self.__MaxValue = 0
        self.__groupRange = 0
    
        self.__values = []
        self.__interv = []

    def getInterv(self):
        return self.__interv

    def setNumInterv(self, value):
        self.__NumIntr = value

    def getNumInterv(self):
        return self.__NumIntr

    def add(self, value):
        self.__values.append(value)

    def __getGroupRange(self):
        diff = self.__MaxValue - self.__MinValue

        if  diff < 10:
            return 2
        elif diff >= 10 and diff < 20:
            return 5
        elif diff >= 20:
            return 10
        

    def __group(self):
        self.__values.sort()
        self.__MinValue, self.__MaxValue = self.__values[0], self.__values[self.getSize() - 1]

        i = self.__MinValue
        self.__groupRange = self.__getGroupRange()
        
        while i < (self.__MaxValue + self.__groupRange) :
            self.__interv.append(intervalo(i, (i + (self.__groupRange - 1)) ))
            i += self.__groupRange
        
    def calc(self):
        self.__group()

        for i in self.__interv:
            i.setClassMark(self.ClassMark(i.getXmin(), i.getXmax()))

        
    def getSize(self):
        return self.__size
    
    def incrementSize(self):
        self.__size += 1 

    def ClassMark(self, intrMin, intrMax):
        return ( ( intrMin + intrMax ) / 2 )

    def Range(self, X_Min, X_Max):
        return ( X_Max - X_Min )
    
    def Amplitude(self,Range):
        return ( Range / self.__NumIntr )

