import macierz
import komiwojazer
import random
import time





tab = macierz.creatematrix_ATSP()
start = time.clock()
int = random.randint(0, 100)
komi = komiwojazer.Komiwojazer(tab)
#macierz.bruteforce()
#komi.my_main()

end = time.clock()
total = end - start
print("{0:02f}s".format(total))
#komi.display(tab)
#komi.low_bound(tab)
# komi.find_min_in_row_and_column()

#komi.find_max_in_row_and_column()
#komi.find_max_in_min_and_cut()




