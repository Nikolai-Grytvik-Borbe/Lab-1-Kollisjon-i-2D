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
    avvik *= 1/(sluttframe - startframe - 1) # -1 fordi se standardavvik formel
    avvik = sqrt(avvik)
    return avvik


def frames_tid(data, startframe, sluttframe):
    tid = []
    for i in range(startframe, sluttframe):
        tid.append(data[0][i])
    return tid


print("\n")
startframe = 0 # Sett inn verdiene du vil her
sluttframe = 15 #
datasett_studerer = fart1

standardavviket = standardavvik(datasett_studerer, middelverdien(datasett_studerer, startframe, sluttframe), startframe, sluttframe)
avvik_liste = [standardavviket] * len(frames_tid(datasett_studerer, startframe, sluttframe))

print(middelverdien(datasett_studerer, startframe, sluttframe))
print(standardavviket)

# Under har alle error-bars lik lengde fordi jeg har bare satt på standardavviket som y-error, vet ikke hvorfor noen grafer da har error bars med forskjellig lengde, men jaja

plt.errorbar(frames_tid(datasett_studerer, startframe, sluttframe), data_absoluttverdi(datasett_studerer, startframe, sluttframe), yerr = avvik_liste)
plt.show()