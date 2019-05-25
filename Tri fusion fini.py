L = [14,27,23, 27, 12, 1, 34, 5 ]
def Fusion(l1, l2):
    R =[]
    while (l1 != [] and l2 != []):
        if (l1[0] < l2[0]):
            R.append(l1[0])
            del l1[0]
        else:
            R.append(l2[0])
            del l2[0]
    R.extend(l1)
    R.extend(l2)
    return (R)

def tri_Fusion(Tab):
    n = len(Tab)
    if n < 2:
        return (Tab)
    m = int(n/2)
    l = Tab[:m]
    r = Tab[m:]
    ls = tri_Fusion(l)
    rs = tri_Fusion(r)
    return Fusion(ls, rs)