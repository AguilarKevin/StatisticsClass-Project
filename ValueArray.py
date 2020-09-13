from ValueSet import ValueSet

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


    for i in values:
        aux = ValueSet()