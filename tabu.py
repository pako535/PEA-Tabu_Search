import tabulist
class Tabu:

    def __init__(self, tab, lenTabu, cadency):
        self.tab = tab
        self.tabuList = tabulist.TabuList(lenTabu, cadency)
        self.select_start_point(self.tab)
        print("Lista tabu: ", self.tabuList.TList)
        self.find_neighborhood(tab)

    def run(self):
        pass

    @staticmethod
    def select_start_point(tab):

        x0 = []
        value_of_x0 = 0
        dl = len(tab)
        for i in range(dl):
            try:
                value_of_x0 += tab[i][i + 1]
                x0.append(i)
            except:
                value_of_x0 += tab[dl - 1][0]
                x0.append(dl - 1)
                x0.append(0)


        print("Ścieżka: ", x0)
        print("Wartość ścieżki: ", value_of_x0)


    def find_neighborhood(self, tab):
        list_of_move = []
        for i in range(len(tab)):
            for j in range(len(tab)):
                if i != j:
                    tmp = tabulist.Move(j, i)
                    if tmp not in list_of_move: #or tabulist.Move(i, j) in self.tabuList:
                        list_of_move.append(tabulist.Move(i, j))


        print(list_of_move)