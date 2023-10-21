

def slicer(t, e):
    if e not in t:
        return ()

    f_proga = t.index(e)
    s_proga = t.index(e, f_proga + 1)

    return t[f_proga:s_proga + 1]


   


