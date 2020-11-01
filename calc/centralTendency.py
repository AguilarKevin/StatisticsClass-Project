
class CentralTendency(object):

    def __init__(self):
        self.__size = 0

        self.__NumIntr = 0
        self.__MinValue = 0
        self.__MaxValue = 0
    
        self.__values = []
        self.__values_Freq = []
        self.__values_FreqAcum = []
        self.__values_FreqRel = []
        self.__values_FreqPerc = []
        self.__values_ClassMark = []

    def add(self, value):
        self.__values.append(value)

    def size(self):
        return self.__size
    
    def incrementSize(self):
        self.__size += 1 

    def ClassMark(self, IntMin, IntMax):
        return ( ( IntMin + IntMax ) / 2 )

    def Range(self, X_Min, X_Max):
        return ( X_Max - X_Min )
    
    def Amplitude(self,Range):
        return ( Range / self.__NumIntr )

