# Questao 3
import numpy as np
import matplotlib.pyplot as plt

# para o método de newton

a = 4
b = 5
p = 5
rs = []
itMax = 23

def f(x):
  return (x**2) - 23
def df(x):
  return 2*x

def newton(a, b, p, itMax, func, dFunc): # p = erro maximo
  it = 0
  Er = 1
  x1 = a # chute inicial
  while Er > 10**(-p) and it < itMax:
    it = it + 1
    x0 = x1
    x1 = x0 - (f(x0)/df(x0))
    Er = np.abs((x1-x0)/x1)
  return (x1, Er, it, itMax)

rs = newton(a, b, p, itMax, f, df)
print(f'x = {rs[0]}, Er = {rs[1]}, N interações = {rs[2]}')