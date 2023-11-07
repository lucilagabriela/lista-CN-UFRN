import numpy as np

a = float(input())
n = int(input())
x = [float(input()) for x in range(n+1)]
y = [float(input()) for x in range(n+1)]


def newton(x, y):
  n = len(x)
  T = np.zeros((n,n))
  T[:,0] = y
  for j in range(1,n):
    for i in range(0,n-j):
      T[i][j]=(T[i+1][j-1]-T[i][j-1])/(x[i+j]-x[i])
  return T[0,:]

def interpolacaoN(a,x,coef):
  y = coef[0]
  for i in range(1,len(coef)):
    prod = coef[i]
    for j in range(0, i):
      prod = prod*(a - x[j])
    y = y + prod
  return y

bn =  newton(x, y)
PdeA = interpolacaoN(a,x,bn)

soma = PdeA + bn[n]
print(f'{soma:.4f}')