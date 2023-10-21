

def del_from_tuple(t, e):
    if e in t:
        i = t.index(e)
        return t[:i] + t[i+1:]
    else:
        return t


   


