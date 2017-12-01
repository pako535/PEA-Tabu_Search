class TabuList:

    def __init__(self, cadency):
        #self.lenTabuList = lenTabu
        self.cadency = cadency
        self.TList = [] # self.createTabu()



    # def createTabu(self):
    #     TList = []
    #     for i in range(self.lenTabuList):
    #         TList.append(Move(None, None))
    #
    #     return TList

class Move:

    def __init__(self, from_where, to, cadencyMove = None): #, valueOfMove):
        self.from_where = from_where
        self.to = to
        self.cadency = cadencyMove

       # self.valueOfMove = valueOfMove

    def __repr__(self):
        return 'x = %s, y = %s, cadency = %s\n' % (self.from_where, self.to, self.cadency)

    def __eq__(self, other):
        #if isinstance(other,self.__class__):
         #   return self.from_where == other.from_where and self.to == other.to
        #return False
        #return self.__dict__ == other.__dict__

        #return self.from_where == other.from_where and self.to == other.to and self.cadency != other.cadency
        if self.from_where == other.from_where and self.to == other.to:
            return True
        else:
            return False