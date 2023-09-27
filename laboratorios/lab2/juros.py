# Questao 5
import numpy as np
import matplotlib.pyplot as plt

def f1(J):
  # Relação entre valores e juros com parâmetros da 1ª forma
  VP = 2448 # Valor da parcela
  VF = 39000 # Valor financiado
  p = 24 # Prazo em meses
  # J = Taxa de juros
  return 1 - (1 + J)**(-p) - (VF / VP) * J

def f2(J):
  # Relação entre valores e juros com parâmetros da 2ª forma
  VP = 1996 # Valor da parcela
  VF = 39000 # Valor financiado
  p = 36 # Prazo em meses
  # J = Taxa de juros
  return 1 - (1 + J)**(-p) - (VF / VP) * J

def df1(J):
  VP = 2448 # Valor da parcela
  VF = 39000 # Valor financiado
  p = 24 # Prazo em meses
  return p * (J + 1)**(-p) / (J + 1) - (VF / VP)

def df2(J):
  VP = 1996 # Valor da parcela
  VF = 39000 # Valor financiado
  p = 36 # Prazo em meses
  return p * (J + 1)**(-p) / (J + 1) - (VF / VP)


a, b = 0.03, 0.05
x = np.linspace(a, b, 200)
y1 = f1(x)
y2 = f2(x)

plt.plot(x, y1)
plt.plot([a, b], [0, 0])
plt.show()

plt.plot(x, y2)
plt.plot([a, b], [0, 0])
plt.show()

# Questão 6
print(bissec(a, b, 4, 100, f1))
print(falsaPosicao(a, b, 4, 100, f1))
print(newton(a, b, 4, 100, f1, df1))
print(secante(a, b, 4, 100, f1, df1))
print()

# Questão 7
print(bissec(a, b, 4, 100, f2))
print(falsaPosicao(a, b, 4, 100, f2))
print(newton(a, b, 4, 100, f2, df2))
print(secante(a, b, 4, 100, f2, df2))

# Questão 8
print()
a = 0.02
b = 0.06
print(bissec(a, b, 4, 100, f1))
print(falsaPosicao(a, b, 4, 100, f1))
print(newton(a, b, 4, 100, f1, df1))
print(secante(a, b, 4, 100, f1, df1))
print()

# Questão 9

a = 0.02
b = 0.06
print(bissec(a, b, 4, 100, f1))
print(falsaPosicao(a, b, 4, 100, f1))
print(newton(a, b, 4, 100, f1, df1))
print(secante(a, b, 4, 100, f1, df1))
print()