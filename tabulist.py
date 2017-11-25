class TabuList:

    def __init__(self, lenTabu, cadency):
        self.lenTabuList = lenTabu
        self.cadency = cadency
        self.TList = self.createTabu()



    def createTabu(self):
        TList = []
        for i in range(self.lenTabuList):
            TList.append(-1)

        return TList

