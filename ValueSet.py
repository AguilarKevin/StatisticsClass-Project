class ValueSet(object):
    
    def __init__(self, mark, freq):
        self.Mark = mark
        self.Freq = freq

    def incrementFreq(self):
        self.Freq += 1