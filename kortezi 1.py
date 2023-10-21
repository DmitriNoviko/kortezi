def tpl_soft(t):
    if all(isinstance(e, int) for e in t):
        return tuple(sorted(t))
    else:
        return t
s = (4, 2, 3, 1, 5)
print(tpl_soft(s))


   


