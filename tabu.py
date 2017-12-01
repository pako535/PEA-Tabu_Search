import tabulist
import random
import copy
class Tabu:

    def __init__(self, tab, cadency):

        self.currentSolution = 0
        self.tab = tab
        self.cadency = cadency
        self.tabuList = tabulist.TabuList(cadency)
        #self.select_start_point(self.tab)
        print("Lista tabu: ", self.tabuList.TList)
        # self.find_neighborhood(tab)
        self.run()

    def run(self):

        x0 = self.select_start_point(self.tab)
        xopt = x0
        # while(True):
        for i in range(100000):
            resultOfNeighbor = self.find_neighbor(x0)
            if resultOfNeighbor != False:
                x0 = resultOfNeighbor[0]

                if resultOfNeighbor[1] < self.valueOfPath(xopt):
                    xopt = x0


                # try:
                self.verify_tabuList(resultOfNeighbor[2])
                print("Ścieżka: ", resultOfNeighbor[0], "\nWartość: ", resultOfNeighbor[1])
                # except:
                #     print("Ścieżka ta sama: ", resultOfNeighbor[1])

            # CriticalEvent
            else:
                x0 = self.generateNewSolution()


        print("WYNIK: ", self.valueOfPath(xopt), " dla ścieżki: ", xopt)


            

    @staticmethod
    def select_start_point(tab):

        x0 = []
        value_of_x0 = 0
        dl = len(tab)

        # for i in range(dl):
        #     value_of_x0 += min(filter(lambda x: x >= 0, tab[i, :]))


        for i in range(dl):
            try:
                value_of_x0 += tab[i][i + 1]
                x0.append(i)
            except:
                value_of_x0 += tab[dl - 1][0]
                x0.append(dl - 1)



        print("Ścieżka: ", x0)
        print("Wartość ścieżki: ", value_of_x0)
        return x0

    def find_neighbor(self, x0):
        value_of_x0 = 0
        dl = len(x0)
        # Obliczenie wartości cieżki początkowej
        for i in range(len(x0)):
            try:
                value_of_x0 += self.tab[x0[i]][x0[i + 1]]
            except:
                value_of_x0 += self.tab[x0[dl - 1]][x0[0]]

        tmp_value = value_of_x0 + 1
        tmp_path = copy.copy(x0)

        # Znalezienie lepszej scieżki i wyyliczenie jej wartosci
        while(True):
            tmp_value = 0
            #list_of_move = []
            for i in range(len(self.tab)):
                flag = False
                for j in range(len(self.tab)):
                    if i != j:
                        tmp = tabulist.Move(i, j)
                        #if tmp not in list_of_move and tmp not in self.tabuList.TList:     # dopisac czy nie ma na tabu
                        if tmp not in self.tabuList.TList:

                            # SWAP
                            #positions = random.sample(range(dl), 2)
                            tmp = tmp_path[i]
                            tmp_path[i] = tmp_path[j]
                            tmp_path[j] = tmp
                            tmp_value = 0

                            for k in range(len(tmp_path)):

                                try:
                                    tmp_value += self.tab[tmp_path[k]][tmp_path[k + 1]]
                                except:
                                    tmp_value += self.tab[tmp_path[dl - 1]][tmp_path[0]]
                            if tmp_value < value_of_x0:
                                flag = True
                                break
                        if flag == True:
                            break
                if flag == True:
                    break
            if tmp_value < value_of_x0:
                return tmp_path, tmp_value, tabulist.Move(i, j, self.cadency)
            else:
                return False

    def verify_tabuList(self, move):

        # dodaj element do tabuList
        # for i in range(len(self.tabuList.TList)):
        #     if self.tabuList.TList[i] == tabulist.Move(None, None, None):
        #         self.tabuList.TList[i] = move
        #         break
        dl = len(self.tabuList.TList)
        if move != tabulist.Move(None,None,None):
            self.tabuList.TList.append(move)
            self.tabuList.TList.append(tabulist.Move(move.to, move.from_where, move.cadency))


        # dla każdego elementu na tabuList zmniejsz kadencje o 1
        for i in range(len(self.tabuList.TList)):
            # if self.tabuList.TList[i] != tabulist.Move(None, None, None):
            self.tabuList.TList[i].cadency -= 1

        # jesli kadencja = 0 to usun z tabuList
        self.tabuList.TList[:] = [x for x in self.tabuList.TList if x.cadency != 0]

        print(self.tabuList.TList)

    def criticalEvent(self, x0):
        if x0 == self.currentSolution:
            self.noChanges += 1
        self.currentSolution = x0

        if self.noChanges == 4 * len(self.tab):
            return True
        else:
            return False

    def generateNewSolution(self):

        newSolution = []
        listOfVertices = []
        for i in range(len(self.tab)):
            listOfVertices.append(i)

        for i in range(len(self.tab)):
            x = random.choice(listOfVertices)
            index = listOfVertices.index(x)
            listOfVertices.pop(index)
            newSolution.append(x)

        return newSolution

    def valueOfPath(self, x0):
        tmp_value = 0
        dl = len(x0)
        for k in range(len(x0)):

            try:
                tmp_value += self.tab[x0[k]][x0[k + 1]]
            except:
                tmp_value += self.tab[x0[dl - 1]][x0[0]]

        return tmp_value
