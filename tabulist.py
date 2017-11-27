class TabuList:

    def __init__(self, lenTabu, cadency):
        self.lenTabuList = lenTabu
        self.cadency = cadency
        self.TList = self.createTabu()



    def createTabu(self):
        TList = []
        for i in range(self.lenTabuList):
            TList.append(None)

        return TList

class Move:

    def __init__(self, from_where, to): #, valueOfMove):
        self.from_where = from_where
        self.to = to
       # self.valueOfMove = valueOfMove

    def __repr__(self):
        return 'x=%s, y=%s\n' % (self.from_where, self.to)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__