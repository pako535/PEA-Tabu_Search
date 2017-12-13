import macierz
import tabu
import random
import time
import  tests





tab = macierz.creatematrix_TSP('gr120.tsp')
#tab = macierz.creatematrix_ATSP('atsp15.txt')
start = time.clock()
int = random.randint(0, 100)

print(tab, "\n\n")
TS = tabu.Tabu(tab, 7, 1000)


end = time.clock()
total = end - start
print("{0:02f}s".format(total))




