import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return np.exp(x)*np.cos(x-1)

def df(x):
  return np.exp(x)*np.cos(x-1)-np.exp(x)*np.sin(x-1)

def df2(x):
  return -2*np.exp(x)*np.sin(x-1)

def df3(x):
  return -2*np.exp(x)*np.sin(x-1)-2*np.exp(x)*np.cos(x-1)

def p2(x):
  x0 = 2.8
  return f(x0) + df(x0)*(x-x0) + (df2(x0)/2)*(x-x0)**2

def Resto(t):
  x0 = 2.8
  x = 3.0
  return (df3(t)*(x-x0)**3)/6

xg = np.linspace(2, 3.5, 100)
ygf = f(xg)
ygp2 = p2(xg)

plt.plot(xg, ygf) #plt.show() logo depois do plot pra mostrar o outro plot em outra imagem se necessário
plt.plot(xg, ygp2)
plt.grid()
plt.show()

Erro = np.abs(f(3.0) - p2(3.0))
print("O erro eh: ", Erro)

print("P2: ", p2(3.0))

tau = np.linspace(2.8, 3, 50)
yResto = Resto(tau)
plt.plot(tau, yResto)
plt.show()

ErroMax = np.abs(Resto(2.8))
print("Erro Maximo = ", ErroMax)

ErroAbs = np.abs(f(3) - p2(3))
print("Erro Absoluto = ", ErroAbs)
