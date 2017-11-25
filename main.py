import macierz

import random
import time





tab = macierz.creatematrix_ATSP()
start = time.clock()
int = random.randint(0, 100)


end = time.clock()
total = end - start
print("{0:02f}s".format(total))




