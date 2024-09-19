import numpy as np

def get_data() -> list[list]:
    """
    Returns formatted data

    Returns:
        list: -> [time], [puck1], [puck2]
    """

    data  = np.loadtxt("ResultatKollisjon1.csv", delimiter=";")
    time  = []
    puck1 = []
    puck2 = []

    time  = data[:,0].tolist()
    puck1 = [time, data[:,1].tolist(), data[:,2].tolist()]
    puck2 = [time, data[:,3].tolist(), data[:,4].tolist()]

    return [puck1, puck2]

def get_puck1():
    data = get_data()
    puck1 = data[0]
    
    return puck1 

def get_puck2():
    data = get_data()
    puck2 = data[1]
    
    return puck2 
