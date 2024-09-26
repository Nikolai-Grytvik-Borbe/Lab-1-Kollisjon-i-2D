import numpy as np
import matplotlib.pyplot as plt
from get_data import *
from derivasjon import *


def beregning(posisjoner: list[list]):
    """
    The beregning function calculates and optionally plots the velocity and acceleration from position data. It returns the velocity and acceleration. 
    """
    fart = [posisjoner[0], [], []] # Lager tomt fartsarray som skal ha verdiene t, v_x, v_y

    posisjon_derivering(posisjoner,fart)

    akselerasjon = [fart[0], [], []]

    fart_derivering(fart, akselerasjon)

    # Første del i lista er bare t-verdiene
    abspos = [posisjoner[0],[]] # Beregner absoluttposisjon (gir dette mening?)
    absfart = [fart[0],[]] # Beregner absoluttfart
    absaks = [akselerasjon[0],[]] # Beregner absoluttakselerasjon

    for i in range(len(posisjoner[0])):
        abspos[1].append(np.sqrt(posisjoner[1][i]**2+posisjoner[2][i]**2))
    for i in range(len(fart[0])):
        absfart[1].append(np.sqrt(fart[1][i]**2+fart[2][i]**2))
    for i in range(len(akselerasjon[0])):
        absaks[1].append(np.sqrt(akselerasjon[1][i]**2+akselerasjon[2][i]**2))


    return fart, akselerasjon

"""
data1 = beregning(get_puck1())
data2 = beregning(get_puck2())
plt.plot(data1[0], data1[1], "c", label="Disk 1")
plt.plot(data2[0], data2[1], "--m", label="Disk 2")
plt.xlabel("Tid $(s)$")
plt.ylabel("Akselerasjon $({cm}/{s^2})$")
plt.legend()
plt.show()
"""