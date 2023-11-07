#questão 3 Multiprova
# atenção corrigir os valores dos pontos conforme sua questao


import numpy as np

x = [44, 62, 82, 99]

y = [15.5, 15.1, 12.9, 10.2]


p = 71
n = 3

def p_erro(x0,x1,x2,erro,p):
  return(erro*(p-x0)*(p-x1)*(p-x2))

def CTDD (x,y):
  n = np.size(x)
  T = np.zeros((n,n))
  for i in range (n):
    T[i,0] = y[i]
  for j in range(1,n):
    for i in range(n-j):
      T[i,j] = (T[i+1,j-1] - T[i,j-1]) / (x[i+j] - x[i])
  return T

TDD= CTDD (x,y)

print(TDD)

def P_Newton(x,y,n,p):
  T = CTDD (x,y)
  Soma = T[0,0]
  for i in range(1,n+1):
    M = T[0,i]
    for j in range(i):
      M = M*(p-x[j])
    Soma = Soma + M
  return Soma

T = CTDD (x,y)

S = P_Newton(x,y,n,p)

bn = T[0,n]

print(f'{bn:.10f}')
print(f'polinomio de erro',p_erro(x[0],x[1],x[2],T[0,n],p))
print(f'{S:.6f}')