from data_plot import *
from constants import MASSE1, MASSE2

posisjon1 = get_puck1()
posisjon2 = get_puck2()

fart1, akselerasjon1 = beregning(posisjon1, "1", False)
fart2, akselerasjon2 = beregning(posisjon2, "2", False)

tid = posisjon1[0]
bevegelsesmengde_x = []
bevegelsesmengde_y = []

for i in range(len(tid)): # Beregner bevegelsesmengde i x og y retning
    bevegelsesmengde_x.append(MASSE1*fart1[1][i]+MASSE2*fart2[1][i])
    bevegelsesmengde_y.append(MASSE1*fart1[2][i]+MASSE2*fart2[2][i])

bevegelsesmengde_total = []
for i in range(len(tid)):
    bevegelsesmengde_total.append(np.sqrt(bevegelsesmengde_x[i]**2+bevegelsesmengde_y[i]**2))

plt.plot(tid, bevegelsesmengde_total, "r", label="Bevegelsesmengde")
plt.xlabel("Tid $(s)$")
plt.ylabel("Bevegelsesmengde $({m}\\cdot{v})$")
plt.legend()
plt.grid(True)
plt.show()