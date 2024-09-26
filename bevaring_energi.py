import numpy as np
import matplotlib.pyplot as plt
from constants import MASSE1, MASSE2, kalk_energi
from get_data import get_puck1, get_puck2
from data_plot import beregning

posisjon1 = get_puck1()
posisjon2 = get_puck2()


fart1, akselerasjon1 = beregning(posisjon1)
tot_fart1 = [np.sqrt(x**2 + y**2) for x, y in zip(fart1[1], fart1[2])]

fart2, akselerasjon2 = beregning(posisjon2)
tot_fart2 = [np.sqrt(x**2 + y**2) for x, y in zip(fart2[1], fart2[2])]


def endring_energi(data, masse) -> list[list]:
    """
    Hvor data skal være: [[tid], [fart_x], [fart_y]]

    Returnerer: [[tid], [energi]]
    """

    tider  = data[0]
    vx     = data[1]
    vy     = data[2]
    np_energi = []

    for i in range(len(tider)):
        v_tot = np.sqrt(vx[i]**2 + vy[i]**2)
        np_energi.append(0.5*masse*v_tot**2)

    energi = [float(i) for i in np_energi] # np.float -> python float
    
    return [tider, energi]


tider, energi1 = endring_energi(fart1, MASSE1)   # <- unpacker tider og energi fra endring_energi()
_, energi2 = endring_energi(fart2, MASSE2)       # <- Samme, men bruker ikke tidene herifra

sum_energi = [energi1[i]+energi2[i] for i in range(len(energi1))]

plt.plot(tider, energi1, "--r", label="Energi disk 1")
plt.plot(tider, energi2, "--b", label="Energi disk 2")
plt.plot(tider, sum_energi, "g", label="Sum")
plt.legend()
plt.grid(True)
plt.show()



def er_energi_konservert(E_før: int, E_etter: int, toleranse = 1e-5) -> bool:
    endring = abs(E_før - E_etter)

    if endring < toleranse:
        print(f"Endring i energi: {endring}, som ligger innenfor toleransen på {toleranse}.")
        return True
    elif endring > toleranse:
        print(f"Endringen i energi: {endring}, ligger utenfor toleransen på {toleranse}.")
        return False
    else:
        raise ValueError("Manglende data")

        
# Er energi konservert?

# kollisjon skjer på iteration 17 men dataen øker litt før
avg_fart1_før       = sum(tot_fart1[0:15])/15
avg_fart1_etter     = sum(tot_fart1[20:40])/20
avg_fart2_før       = sum(tot_fart2[0:15])/15
avg_fart2_etter     = sum(tot_fart2[20:40])/20

energi_før          = kalk_energi((MASSE1, avg_fart1_før), (MASSE2, avg_fart2_før))
energi_etter        = kalk_energi((MASSE1, avg_fart1_etter), (MASSE2, avg_fart2_etter))

print(er_energi_konservert(energi_før, energi_etter, toleranse = 10))





























