import numpy as np
import matplotlib.pyplot as plt
from get_data import *



def plot_graph(x, y, Label = "f"): #Plotter inn grafen i et koordinatsystem
    plt.plot(x,y, "--", label = Label)
    plt.legend()

def beregning(posisjon, pucknr):
    fart = [posisjon[0], [], []] # Lager tomt fartsarray som skal ha verdiene t, v_x, v_y

    def posisjon_derivering(): # Deriverer posisjonsdataen med hensyn på t
        for i in range(len(posisjon[0])): # Like mange iterasjoner som t-verdier i arrayet
            if i == 0:
                #Fart i første 10 ms
                vx = (posisjon[1][i+1]-posisjon[1][i])/(posisjon[0][i+1]-posisjon[0][i]) # Gjennomsnittlig fart fra posisjon tid t = 0 til t = 0.01
                vy = (posisjon[2][i+1]-posisjon[2][i])/(posisjon[0][i+1]-posisjon[0][i])
                fart[1].append(vx)
                fart[2].append(vy)
            elif (len(posisjon[0])-1) > i > 0:
                # Fart resten av tida, her regner jeg gj. snitt fart fra bilde før til bilde etter det aktuelle bildetidspunktet, slik at farta blir mest mulig korrekt.
                vx = (posisjon[1][i+1]-posisjon[1][i-1])/(posisjon[0][i+1]-posisjon[0][i-1]) # Gjennomsnittlig fart fra posisjon tid t -= 0.01 til t += 0.01
                vy = (posisjon[2][i+1]-posisjon[2][i-1])/(posisjon[0][i+1]-posisjon[0][i-1])
                fart[1].append(vx)
                fart[2].append(vy)
            else:
                #Fart i siste 10ms
                vx = (posisjon[1][i]-posisjon[1][i-1])/(posisjon[0][i]-posisjon[0][i-1]) # Gjennomsnittlig fart fra posisjon tid t = t_max-0.01 til t = t_max
                vy = (posisjon[2][i]-posisjon[2][i-1])/(posisjon[0][i]-posisjon[0][i-1])
                fart[1].append(vx)
                fart[2].append(vy)

    akselerasjon = [fart[0], [], []]

    def fart_derivering(): # Deriverer posisjonsdataen med hensyn på t
        for i in range(len(posisjon[0])): # Like mange iterasjoner som t-verdier i arrayet
            if i == 0:
                #Fart i første 10 ms
                ax = (fart[1][i+1]-fart[1][i])/(fart[0][i+1]-fart[0][i]) # Gjennomsnittlig fart fra posisjon tid t = 0 til t = 0.01
                ay = (fart[2][i+1]-fart[2][i])/(fart[0][i+1]-fart[0][i])
                akselerasjon[1].append(ax)
                akselerasjon[2].append(ay)
            elif (len(posisjon[0])-1) > i > 0:
                # Fart resten av tida, her regner jeg gj. snitt fart fra bilde før til bilde etter det aktuelle bildetidspunktet, slik at farta blir mest mulig korrekt.
                ax = (fart[1][i+1]-fart[1][i-1])/(fart[0][i+1]-fart[0][i-1]) # Gjennomsnittlig fart fra posisjon tid t -= 0.01 til t += 0.01
                ay = (fart[2][i+1]-fart[2][i-1])/(fart[0][i+1]-fart[0][i-1])
                akselerasjon[1].append(ax)
                akselerasjon[2].append(ay)
            else:
                #Fart i siste 10ms
                ax = (fart[1][i]-fart[1][i-1])/(fart[0][i]-fart[0][i-1]) # Gjennomsnittlig fart fra posisjon tid t = t_max-0.01 til t = t_max
                ay = (fart[2][i]-fart[2][i-1])/(fart[0][i]-fart[0][i-1])
                akselerasjon[1].append(ax)
                akselerasjon[2].append(ay)
    posisjon_derivering()
    fart_derivering()

    abspos = [posisjon[0],[]] # Beregner absoluttposisjon (gir dette mening?)
    absfart = [fart[0],[]] # Beregner absoluttfart
    absaks = [akselerasjon[0],[]] # Beregner absoluttakselerasjon

    for i in range(len(posisjon[0])):
        abspos[1].append(np.sqrt(posisjon[1][i]**2+posisjon[2][i]**2))
    for i in range(len(fart[0])):
        absfart[1].append(np.sqrt(fart[1][i]**2+fart[2][i]**2))
    for i in range(len(akselerasjon[0])):
        absaks[1].append(np.sqrt(akselerasjon[1][i]**2+akselerasjon[2][i]**2))



    plot_graph(abspos[0],abspos[1], f"Posisjon {pucknr}")
    plot_graph(absfart[0],absfart[1], f"Fart {pucknr}")
    #plot_graph(absaks[0],absaks[1], f"Akselerasjon {pucknr}")
    return fart, akselerasjon
beregning(get_puck1(), "1")
beregning(get_puck2(), "2")
plt.show()
print(get_puck1())