from model.Interval import Interval

class FrequencyTable(object):

    def __init__(self, minValue, maxValue, amplitude, valuesList, numIntervals):
        self.__intervals = []
        self.__width = amplitude
        self.__minValue = minValue
        self.__maxValue = maxValue
        self.__values = valuesList
        self.__numIntervals = numIntervals

    def getIntervals(self):
        self.__createIntervals()
        return self.__createFrequenceTable()

    def __classMark(self, intrMin, intrMax):
        return ( ( intrMin + intrMax ) / 2 )

    def __frequence(self, intrMin, intrMax):
        frequence = 0
        i = intrMin

        while i <= intrMax:
            frequence += self.__values.count(i)
            i += 1

        return frequence

    def __accumulatedFrequency(self, freq1, freq2 ):
        return (freq1 + freq2)

    def __relativeFrequency(self, freq):
        return (freq / len(self.__values))

    def __percentageFrequency(self, freq):
        return ((freq / len(self.__values)) * 100)

    def __createIntervals(self):
        
        i, increment = self.__minValue, (self.__width - 1)
        
        while i <= self.__maxValue :
            self.__intervals.append(Interval(i, (i + increment) ))
            i += self.__width

    def __createFrequenceTable(self):
    
        i = aux = 0
        while i < len(self.__intervals):
            self.__intervals[i].setClassMark(self.__classMark(self.__intervals[i].getXmin(), self.__intervals[i].getXmax()))
            self.__intervals[i].setFreq(self.__frequence(self.__intervals[i].getXmin(), self.__intervals[i].getXmax()))

            if i > 0:
                aux = self.__intervals[i-1].getAccumFreq()
                print(aux)

            self.__intervals[i].setAccumFreq( self.__accumulatedFrequency(aux, self.__intervals[i].getFreq()) )
            self.__intervals[i].setRelativeFreq(self.__relativeFrequency(self.__intervals[i].getFreq()))
            self.__intervals[i].setPercFreq(self.__percentageFrequency(self.__intervals[i].getFreq()))

            print(self.__intervals[i].get())
            print("index"+str(i))
            i += 1


        self.__intervals.reverse()
        return self.__intervals

