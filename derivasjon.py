import numpy as np

def posisjon_derivering(posisjon, fart): # Deriverer posisjonsdataen med hensyn på t
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
            vy = (posisjon[2][i]-posisjon[2][i-1])/(posisjon[0][i]-posisjon[0][i-1]) # litt feil, dgb
            fart[1].append(vx)
            fart[2].append(vy)
    return fart

def fart_derivering(fart, akselerasjon): # Deriverer posisjonsdataen med hensyn på t
    for i in range(len(fart[0])): # Like mange iterasjoner som t-verdier i arrayet
        if i == 0:
            #Fart i første 10 ms
            ax = (fart[1][i+1]-fart[1][i])/(fart[0][i+1]-fart[0][i]) # Gjennomsnittlig fart fra posisjon tid t = 0 til t = 0.01
            ay = (fart[2][i+1]-fart[2][i])/(fart[0][i+1]-fart[0][i])
            akselerasjon[1].append(ax)
            akselerasjon[2].append(ay)
        elif (len(fart[0])-1) > i > 0:
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
    return akselerasjon