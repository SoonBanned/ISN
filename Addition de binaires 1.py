import numpy
Longueur = int(input("Quelle taille de binaire ?"))
a = numpy.random.choice([0, 1], size=(Longueur,), p=[1/3, 2/3])
b = numpy.random.choice([0, 1], size=(Longueur,), p=[1/3, 2/3])
print ("Debug >> ",a)
print ("Debug >> ",b)

def Addition_binaires(Bin1, Bin2):
    global Sb
    Sb = []
    b = 0
    for i in range (0,Longueur):
        Sb.append(Bin1[i] + Bin2[i])

    while b != 1:
        for i in range (0, len(Sb)):
            if Sb[i] == 2:
                if i == 0:
                    Sb.insert(0, 1)
                    Sb[1] = 0
                else:
                    Sb[i] = 0
                    Sb[i-1] += 1
        if (Sb.count(2) == 0):
            b = 1

Addition_binaires(a,b)
print(Sb)