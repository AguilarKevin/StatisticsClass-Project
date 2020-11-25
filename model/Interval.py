class Interval(object):

    def __init__(self, Xmin, Xmax):
        self.__Xmin = Xmin
        self.__Xmax = Xmax
        self.__freq = 0
        self.__accumFreq = 0
        self.__relativeFreq = 0
        self.__percentFreq = 0
        self.__classMark = 0

    def get(self):
        return "{:.3f}".format(self.__Xmin)+ "-" + "{:.3f}".format(self.__Xmax) + " " + \
            "{:.3f}".format(self.__classMark)  + " " + "{:.3f}".format(self.__freq) + " " +\
                "{:.3f}".format(self.__accumFreq) + " " + "{:.3f}".format(self.__relativeFreq) \
                    + " " + "{:.3f}".format(self.__percentFreq)

    def getXmin(self):
        return self.__Xmin

    def getXmax(self):
        return self.__Xmax

    def setFreq(self, value):
        self.__freq = value

    def getFreq(self):
        return self.__freq

    def setAccumFreq(self, value):
        self.__accumFreq = value

    def getAccumFreq(self):
        return self.__accumFreq

    def setRelativeFreq(self, value):
        self.__relativeFreq = value

    def getRelativeFreq(self):
        return self.__relativeFreq

    def setPercFreq(self, value):
        self.__percentFreq = value

    def getPercFreq(self):
        return self.__percentFreq

    def setClassMark(self, value):
        self.__classMark = value

    def getClassMark(self):
        return self.__classMark