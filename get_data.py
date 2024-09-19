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

    time  = data[:,0]
    puck1 = [time, data[:,1], data[:,2]]
    puck2 = [time, data[:,3], data[:,4]]

    return [puck1, puck2]

def get_puck1():
    data = get_data()
    puck1 = data[0]
    
    return puck1 

def get_puck2():
    data = get_data()
    puck2 = data[1]
    
    return puck2 
print(get_puck1())