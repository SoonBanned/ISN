L = [5,86,69,73,11,17,1,74,34,3]
def tri_Rapide(Tab):
    if Tab == []:
        return []
    else:
        pivot = Tab[0]
        t1 = []
        t2 = []
        for x in Tab[1:]:
            if x<pivot:
                t1.append(x)
            else:
                t2.append(x)
    return tri_Rapide(t1)+[pivot]+tri_Rapide(t2)