import tabulist
class Tabu:

    def __init__(self, tab, lenTabu, cadency):
        self.tab = tab
        self.tabuList = tabulist.TabuList(lenTabu, cadency)
        self.select_start_point(self.tab)

    def select_start_point(self, tab):

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


