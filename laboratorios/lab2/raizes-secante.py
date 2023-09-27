# Questao 4
import numpy as np
import matplotlib.pyplot as plt

# para o método da secante

a = 4
b = 5
p = 5
rs = []
itMax = 20

def f(x):
  return (x**2) - 17

def secante(a, b, p, itMax, func, dFunc): # p = erro maximo
  it = 0
  Er = 1
  x0 = a # chute inicial
  x1 = b
  while Er > 10**(-p) and it < itMax:
    x2 = (x0*f(x1) - x1*f(x0))/(f(x1)-f(x0))
    it = it + 1
    x0 = x1
    x1 = x2
    Er = np.abs((x1-x0)/x1)
  return (x2, Er, it, itMax)

rs = secante(a, b, p, itMax, f, df)
print(f'x = {rs[0]}, Er = {rs[1]}, N interações = {rs[2]}')