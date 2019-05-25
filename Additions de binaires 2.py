import numpy

Longueur = int(input("Quelle taille de binaire ?"))

a = numpy.random.choice([0, 1], size=(Longueur,), p=[1/3, 2/3])
b = numpy.random.choice([0, 1], size=(Longueur,), p=[1/3, 2/3])

print ("Debug >> ",a)
print ("Debug >> ",b)

def Addition_binaires(Bin1, Bin2):
    global Sb
    Sb = []
    S = 0

    for i in range (0,Longueur):
        t = Bin1[i] + Bin2[i]
        S += t * (2**(Longueur-i-1))

    for i in range (0, Longueur + 1):
        if S >= 2**(Longueur-i):
            Sb.append(1)
            S -= 2**(Longueur-i)
        else:
            Sb.append(0)

Addition_binaires(a,b)
print(Sb)