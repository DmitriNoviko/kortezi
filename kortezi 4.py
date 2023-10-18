'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def del_from_tuple(t, e):
    if e in t:
        i = t.index(e)
        return t[:i] + t[i+1:]
    else:
        return t


   


