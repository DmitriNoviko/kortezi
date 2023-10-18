'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def tpl_soft(t):
    if all(isinstance(e, int) for e in t):
        return tuple(sorted(t))
    else:
        return t
s = (4, 2, 3, 1, 5)
print(tpl_soft(s))


   


