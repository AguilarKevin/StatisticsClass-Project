class ValueSet(object):

    Mark = 0
    Freq = 0
    
    def __init__(self, mark, freq):
        self.Mark = mark
        self.Freq = freq

    def incrementFreq(self):
        self.Freq += 1