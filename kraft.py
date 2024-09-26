from data_plot import *
from constants import MASSE1, MASSE2

posisjon1 = get_puck1()
posisjon2 = get_puck2()

fart1, akselerasjon1 = beregning(posisjon1, "1", False)
fart2, akselerasjon2 = beregning(posisjon2, "2", False)
print(fart1[0])