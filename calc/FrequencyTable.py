class FrequencyTable(object):

    def __init__(self, width):
        self.__intervals = []
        self.__Width = width

    
    def getIntervals(self):
        self.__intervals.reverse()
        return self.__intervals

    def setNumIntervals(self, value):
        self.__NumIntr = value

    def ClassMark(self, intrMin, intrMax):
        return ( ( intrMin + intrMax ) / 2 )

    def frequence(self, intrMin, intrMax):
        frequence = 0
        i = intrMin

        while i <= intrMax:
            frequence += self.__values.count(i)
            i += 1

        return frequence

    def accumulatedFrequency(self, freq1, freq2 ):
        return freq1 + freq2

    def relativeFrequency(self, freq):
        return freq / self.__NumIntr

    def percentageFrequency(self, freq):
        return ((freq / self.__NumIntr) * 100)


    def createIntervals(self):
        pass

    def createFrequenceTable(self):
    
        i = aux = 0
        while i < len(self.__intervals):
            if i > 0:
                aux = self.__intervals[i-1].getFreqAcum()

            self.__intervals[i].setClassMark(self.ClassMark(self.__intervals[i].getXmin(), self.__intervals[i].getXmax()))
            self.__intervals[i].setFreq(self.frequence(self.__intervals[i].getXmin(), self.__intervals[i].getXmax()))
            self.__intervals[i].setFreqAcum(self.accumulatedFrequency(aux, self.__intervals[i].getFreq()))
            self.__intervals[i].setFreqRel(self.relativeFrequency(self.__intervals[i].getFreq()))
            self.__intervals[i].setFreqPerc(self.percentageFrequency(self.__intervals[i].getFreq()))

            i += 1

