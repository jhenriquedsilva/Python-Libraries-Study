"""
import numpy as np
# data = {i : np.random.randn() for i in range(7)}
def f(x,y,z):
    return (x + y) / z

a = 7
b = 9
c = 7.5

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False


x = (1,2,23,4)

if not isinstance(x, list) and isiterable(x):
    x = list(x)

result = f(a,b,c)
# %load -> imports a script into a code cell
# %run -> runs a code
# %paste takes whatever text is in the clipboard and executes it as a single block in the shell
# %cpaste is similar, except that it gives you a special prompt for pasting code into
# print(data)
# print("Hello world!")
# to check if two variable refer to the same object, use the IS operator

x = 5
y = 7
print(isinstance(x,(int,float,bool)))
if x > 5:
    x += 1
    y = 8
print(x,y)

"""
x = 0
if x < 0:
    print('Negative!')
elif x == 0:
    pass # do nothing instruction
else: 
    print('Positive!')

preco = 4
value = "Barato" if preco < 5 else "Caro"
print(value)