import macierz
import tabu
import random
import time





tab = macierz.creatematrix_ATSP()

start = time.clock()
int = random.randint(0, 100)

print(tab, "\n\n")
TS = tabu.Tabu(tab, 3, 3)


end = time.clock()
total = end - start
print("{0:02f}s".format(total))




