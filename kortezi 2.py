'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def slicer(t, e):
    if e not in t:
        return ()

    f_proga = t.index(e)
    s_proga = t.index(e, f_proga + 1)

    return t[f_proga:s_proga + 1]


   


