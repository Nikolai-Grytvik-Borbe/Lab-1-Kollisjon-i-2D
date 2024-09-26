from data_plot import *
from constants import MASSE1, MASSE2
from math import sqrt

posisjon1 = get_puck1()
posisjon2 = get_puck2()

fart1, akselerasjon1 = beregning(posisjon1)
fart2, akselerasjon2 = beregning(posisjon2)

startframe = 0
sluttframe = len(posisjon1[0])


def fart_til_absfart(fart, startframe, sluttframe):
    absfart = []
    for i in range(startframe, sluttframe):
        absfart.append(sqrt(fart[1][i]**2+fart[2][i]**2))
    return absfart

def middelverdien(fart, startframe, sluttframe):
    absfart = fart_til_absfart(fart, startframe, sluttframe)

    middelverdi = 0

    for i in range(len(absfart)):
        middelverdi += absfart[i]
    middelverdi *= 1/len(absfart)
    return middelverdi


def standardavvik(fart,middelverdi, startframe, sluttframe):
    absfart = fart_til_absfart(fart, startframe, sluttframe)

    avvik = 0

    for i in range(startframe, sluttframe):
        avvik += (absfart[i]-middelverdi)**2
    avvik *= 1/(sluttframe - startframe)
    avvik = sqrt(avvik)
    return avvik
        


print("\n")

print(middelverdien(fart1, 0, 15))

print(standardavvik(fart1, middelverdien(fart1, 0, 16), 0, 1))