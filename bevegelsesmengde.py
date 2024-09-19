from data_plot import *

posisjon1 = get_puck1()
posisjon2 = get_puck2()

fart1, akselerasjon1 = beregning(posisjon1, "1", False)
fart2, akselerasjon2 = beregning(posisjon2, "2", False)
m1 = 0.031638 # 30 gram
m2 = 0.029797

tid = posisjon1[0]
bevegelsesmengde_x = []
bevegelsesmengde_y = []

for i in range(len(tid)): # Beregner bevegelsesmengde i x og y retning
    bevegelsesmengde_x.append(m1*fart1[1][i]+m2*fart2[1][i])
    bevegelsesmengde_y.append(m1*fart1[2][i]+m2*fart2[2][i])

bevegelsesmengde_total = []
for i in range(len(tid)):
    bevegelsesmengde_total.append(np.sqrt(bevegelsesmengde_x[i]**2+bevegelsesmengde_y[i]**2))

plot_graph(tid,bevegelsesmengde_total)
plt.show()