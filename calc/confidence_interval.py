class ConfidenceInterval():

    def __init__(self):
        self.alpha = 0
        self.standartDeviation = 0
        self.median = 0
        self.n = 0

    def setAlpha(self, value):
        self.alpha = value

    def setStandartDeviation(self, value):
        self.standartDeviation = value

    def set_N(self, value):
        self.n = value

    def setMedian(self, value):
        self.median = value