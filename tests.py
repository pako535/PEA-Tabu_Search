import random
import time
import tabu
import macierz

#
#
# sciezka = ['br17.atsp']#['ftv33.atsp', 'ftv47.atsp', 'ftv55.atsp', 'ftv70.atsp']#, 'ftv170.atsp']
# kadencje = [1]
# itercje = [1000, 5000, 10000]
#
# for i in range(len(sciezka)):
#     plik = open(sciezka[i][:-5] + '77.txt', 'w')
#     tab = macierz.creatematrix_ATSP(sciezka[i])
#     for j in range(len(kadencje)):
#         kadencja = kadencje[j]
#         for k in range(len(itercje)):
#             total = 0
#             suma = 0
#             #for z in range(3):
#             start = time.clock()
#             int = random.randint(0, 100)
#             TS = tabu.Tabu(tab, 7, itercje[k])
#             end = time.clock()
#             total += end - start
#             suma += TS.www
#           #  total = total/3
#           #  suma = suma/3
#             wynik = str(sciezka[i]) + ' ' + ' najlepszy znaleziony wynik: '+ str(suma) + ' ' + str(total) + 's' + ' kedencje ' + str(kadencje[j]) + ' iteracje '+ str(itercje[k])
#             print("Scieżka: ", sciezka[i], "\nKadencja: ", kadencje[j], "\nIteracje: ", itercje[k])
#             plik.writelines(wynik)
#     plik.close()
# #
# TSP
#
sciezka = ['gr120.tsp']#,#']gr17.tsp', 'gr24.tsp', 'gr48.tsp' #,
kadencje = [3, 2, 1]
itercje = [1000, 5000, 10000]

for i in range(len(sciezka)):
    plik = open(sciezka[i][:-4] + '.txt', 'w')
    tab = macierz.creatematrix_TSP(sciezka[i])
    for j in range(len(kadencje)):
        kadencja = kadencje[j]
        for k in range(len(itercje)):
            total = 0
            suma = 0

            start = time.clock()
            int = random.randint(0, 100)
            TS = tabu.Tabu(tab, len(tab) // kadencje[j], itercje[k])
            end = time.clock()
            total += end - start
            suma += TS.www

            wynik = str(sciezka[i]) + ' ' + ' najlepszy znaleziony wynik: '+ str(suma) + ' ' + str(total) + 's' + ' kedencje ' + str(kadencje[j]) + ' iteracje '+ str(itercje[k])
            print("Scieżka: ", sciezka[i], "\nKadencja: ", kadencje[j], "\nIteracje: ", itercje[k])
            plik.writelines(wynik)
    plik.close()


