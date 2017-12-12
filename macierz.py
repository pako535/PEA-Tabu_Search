from numpy import*
import linecache
import itertools
import sys
import math

def creatematrix_TSP(sciezka):

    file = 'tsp/' + sciezka
    tekst = open(file).read()
    # print(tekst)
    tekst = tekst.split()
    tekst = tekst[19:]
    # print(tekst)

    dl = len(tekst)

    dimension = linecache.getline(file, 4)
    dimension = dimension[11:]
    dimension = int(dimension)

    tab = zeros((dimension, dimension), int)
    # print(tab)

    # wpisywanie do macierzy odległosci jako int a nie str
    counter = 0

    infinity = -1

    for i in range(dimension):
        j = 0
        k = False
        while(True):
            if tekst[counter] == '0':
                tekst[counter] = infinity
            tab[i][j] = int(tekst[counter])
            tab[j][i] =int(tekst[counter])
            counter += 1
            j += 1
            k = True
            if not(tekst[counter - 1] != infinity and counter - 1 < dl):
                break

        if k == False:
             counter += 1

    # for i in range(dimension):
    #     tab[0, 1 + i:] = i
    #     tab[1 + i:, 0] = i
    #
    #     tab[0][0] = -2
    #print(tab)
    return tab


def creatematrix_ATSP(sciezka):
    file = 'atsp/' + sciezka      # + 'ftv70.atsp'
    tekst = open(file).read()

    #print(tekst)
    tekst = tekst.split()
    #print(tekst)
    tekst = tekst[16:]
    #print(tekst)

    dl = len(tekst)

    dimension = linecache.getline(file, 4)
    dimension = dimension[11:]
    dimension = int(dimension)

    tab = zeros((dimension, dimension), int)
    # print(tab)

    # wpisywanie do macierzy odległosci jako int a nie str
    counter = 0

    infinity = -1

    for i in range(dimension):
        for j in range(dimension):
            if tekst[counter] =='9999': # '9999':100000000
                tekst[counter] = infinity
            tab[i][j] = int(tekst[counter])
            counter += 1

    # for i in range(dimension):
    #     tab[0, 1+i:] = i
    #     tab[1+i :,0] = i
    #
    # tab[0][0] = -2
    #print(tab)



    return tab


def bruteforce():
    file = 'atsp10.txt'
    tekst = open(file).read()
    tekst = tekst.split()
    tekst = tekst[16:]


    dimension = linecache.getline(file, 4)
    dimension = dimension[11:]
    dimension = int(dimension)

    tab = zeros((dimension , dimension ), int)

    # wpisywanie do macierzy odległosci jako int a nie str
    counter = 0

    infinity = -1

    for i in range(dimension):
        for j in range(dimension):
            if tekst[counter] == '9999':  # '9999':100000000
                tekst[counter] = infinity
            tab[i][j] = int(tekst[counter])
            counter += 1



    dl = range((len(tab)))
    list_of_kombinations = itertools.permutations(dl)
    list_of_value = []
    for p in list_of_kombinations:
        value = 0
        for i in range(len(p)):
            try:
                value += tab[p[i]][p[i + 1]]
            except:
                # if i + 1 != len(tab):
                value += tab[p[i]][p[0]]
        list_of_value.append(value)
    if  file == 'atsp10.txt':
        print(min(list_of_value) + 11)
    else:
        print(min(list_of_value))
