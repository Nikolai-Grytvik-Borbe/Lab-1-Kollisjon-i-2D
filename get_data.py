import numpy as np

def get_data(): 

    data = np.loadtxt("ResultatKollisjon1.txt", delimiter=",")
    print(data)

    puck1 = []
    puck2 = []
    return [puck1, puck2]

get_data()