# brukes til å definere konstanter brukt, så vi vet vi bruker samme data for alt

# Konstanter
MASSE1 = 0.031638 # med utstikk
MASSE2 = 0.029797 # uten utstikk

# Formler
# (litt usikker på om det er bra og ha disse her)
def kalk_energi(*mv_list):
    """
    Returnerer total energi

    mv_list skal være en liste med tuples hvor hver tuple (masse, velocity) er ett energi element
    """

    if len(mv_list) == 0:
        raise ValueError("Manglende data gitt")

    tot_energi = 0
    for m, v in mv_list:
        if m is None or v is None:
            raise ValueError("Minst en tuple har manglende data")
        tot_energi += 0.5*m*v**2
            
    return tot_energi