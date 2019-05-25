def tri_séléction(Tab):
    for i in range (0, len(Tab)):
        a = Tab.index(min(Tab[i:]))
        Tab.insert(i,min(Tab[i:]))
        del Tab[a+1]
    return (Tab)
