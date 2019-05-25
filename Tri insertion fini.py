def Tri_Insertion(Tab):
    LT = len(Tab)
    for i in range (1, LT):
        a = 0
        while Tab[i] > Tab[a]:
            a += 1
        Tab.insert(a, Tab[i])
        del Tab[i+1]
    return (Tab)