# Questao 2
import numpy as np
import matplotlib.pyplot as plt

# para o método da falsa posição

a = 5
b = 6
p = 5 # algarismos significativos
rs = []
itMax = 20

def f(x):
    return (x**2) - 35

def falsaPosicao(a, b, p, itMax, func): # p = erro maximo
    it = 0
    Er = 1
    x1 = a
    while Er > 10**(-p) and it < itMax:
        it = it + 1
        xOld = x1
        x1 = a - (b-a)*func(a)/(func(b)-func(a))
        if (func(a)*func(x1)) < 0:
            b = x1
        else:
            a = x1
        Er = np.abs((x1-xOld)/x1)
    return (x1, Er, it, itMax)

rs = falsaPosicao(a, b, p, itMax, f)
print(f'x1 = {rs[0]}, Er = {rs[1]}, N interações = {rs[2]}')