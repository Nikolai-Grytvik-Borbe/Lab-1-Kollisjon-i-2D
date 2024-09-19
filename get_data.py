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
    puck1 = [data[:,1], data[:,2]]
    puck2 = [data[:,3], data[:,4]]
    return [time, puck1, puck2]