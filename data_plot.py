import numpy as np
import matplotlib.pyplot as plt
from get_data import *
from derivasjon import *


def plot_graph(x, y, Label = "f"): #Plotter inn grafen i et koordinatsystem
    plt.plot(x,y, "--", label = Label)
    plt.legend()

def beregning(posisjoner: list[list], pucknr, plot = False):
    """
    The beregning function calculates and optionally plots the velocity and acceleration from position data. It returns the velocity and acceleration. 
    """
    fart = [posisjoner[0], [], []] # Lager tomt fartsarray som skal ha verdiene t, v_x, v_y

    posisjon_derivering(posisjoner,fart)

    akselerasjon = [fart[0], [], []]

    fart_derivering(fart, akselerasjon)

    abspos = [posisjoner[0],[]] # Beregner absoluttposisjon (gir dette mening?)
    absfart = [fart[0],[]] # Beregner absoluttfart
    absaks = [akselerasjon[0],[]] # Beregner absoluttakselerasjon

    for i in range(len(posisjoner[0])):
        abspos[1].append(np.sqrt(posisjoner[1][i]**2+posisjoner[2][i]**2))
    for i in range(len(fart[0])):
        absfart[1].append(np.sqrt(fart[1][i]**2+fart[2][i]**2))
    for i in range(len(akselerasjon[0])):
        absaks[1].append(np.sqrt(akselerasjon[1][i]**2+akselerasjon[2][i]**2))


    if plot == True:
        plot_graph(abspos[0],abspos[1], f"Posisjon {pucknr}")
        plot_graph(absfart[0],absfart[1], f"Fart {pucknr}")
        plot_graph(absaks[0],absaks[1], f"Akselerasjon {pucknr}")
    return fart, akselerasjon

beregning(get_puck1(), "1", True)
beregning(get_puck2(), "2", True)
plt.show()
