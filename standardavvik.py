from data_plot import *
from constants import MASSE1, MASSE2
from math import sqrt

posisjon1 = get_puck1()
posisjon2 = get_puck2()

fart1, akselerasjon1 = beregning(posisjon1)
fart2, akselerasjon2 = beregning(posisjon2)

startframe = 0
sluttframe = len(posisjon1[0])


def data_absoluttverdi(datasett, startframe, sluttframe):
    abs_datasett = []
    for i in range(startframe, sluttframe):
        abs_datasett.append(sqrt(datasett[1][i]**2+datasett[2][i]**2))
    return abs_datasett

def middelverdien(datasett, startframe, sluttframe):
    abs_datasett = data_absoluttverdi(datasett, startframe, sluttframe)

    middelverdi = 0

    for i in range(len(abs_datasett)):
        middelverdi += abs_datasett[i]
    middelverdi *= 1/len(abs_datasett)
    return middelverdi


def standardavvik(datasett, middelverdi, startframe, sluttframe):
    abs_datasett = data_absoluttverdi(datasett, startframe, sluttframe)

    avvik = 0

    for i in range(sluttframe- startframe):
        avvik += (abs_datasett[i]-middelverdi)**2
    avvik *= 1/(sluttframe - startframe)
    avvik = sqrt(avvik)
    return avvik
        


print("\n")
startframe = 20 # Sett inn verdiene du vil her
sluttframe = 28 #

print(middelverdien(fart1, startframe, sluttframe))
print(standardavvik(fart1, middelverdien(fart1, startframe, sluttframe), startframe, sluttframe))
