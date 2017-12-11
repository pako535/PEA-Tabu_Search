import random
import time
import tabu
import macierz



sciezka = ['ftv33.atsp', 'ftv47.atsp', 'ftv55.atsp', 'ftv70.atsp', 'ftv170.atsp']
kadencje = [3, 2, 1]
itercje = [1000, 5000, 10000]
plik = open('Wyniki.txt', 'w')
for i in range(len(sciezka)):
    tab = macierz.creatematrix_ATSP(sciezka[i])
    for j in range(len(kadencje)):
        kadencja = kadencje[j]
        for k in range(len(itercje)):
            total = 0
            suma = 0
            for z in range(5):
                start = time.clock()
                int = random.randint(0, 100)
                TS = tabu.Tabu(tab, len(tab) // kadencje[j], itercje[k])
                end = time.clock()
                total += end - start
                suma += TS.www
            total = total/5
            suma = suma/5
            wynik = str(sciezka[i]) + ' ' + ' najlepszy znaleziony wynik: '+ str(suma) + ' ' + str(total) + 's' + ' kedencje ' + str(kadencje[j]) + ' iteracje '+ str(itercje[k])

            plik.writelines(wynik)


plik.close()