from data_plot import *
from constants import MASSE1, MASSE2

posisjon1 = get_puck1()
posisjon2 = get_puck2()

fart1, akselerasjon1 = beregning(posisjon1, "1")
fart2, akselerasjon2 = beregning(posisjon2, "2")


def kraft_liste(akselerasjon, masse):
    tid = akselerasjon[0]
    kraft = []

    for i in range(len(tid)): 
        kraft.append(np.sqrt((masse*akselerasjon[1][i])**2 + (masse*akselerasjon[2][i])**2))
        # Beregner kraftsum for hvert tidssteg
            
    return kraft

kraft1 = kraft_liste(akselerasjon1, MASSE1)
kraft2 = kraft_liste(akselerasjon2, MASSE2)

plt.plot(akselerasjon1[0], kraft1)
plt.show()