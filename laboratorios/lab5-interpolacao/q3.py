import numpy as np

x = [60, 81, 95]
y = [15.3, 13, 10.6]

def newton(x, y):
  n = len(x)
  T = np.zeros((n,n))

  T[:,0] = y

  for j in range(1,n):
    for i in range(0,n-j):

      T[i][j]=(T[i+1][j-1]-T[i][j-1])/(x[i+j]-x[i])
  print(T)
  return T[0,:]


def interpolaNewton(A,x,coeficientes):
  y = coeficientes[0]

  for i in range(1,len(coeficientes)):
    produto = coeficientes[i]
    for j in range(0, i):
      produto = produto*(A - x[j])

    y = y+produto

  return y

coeficientes = newton(x,y)
A = 70

print("Coeficientes: ", coeficientes)
print(f"P{len(x)-1}(x) =  ",interpolaNewton(A,x,coeficientes))

print("b2 + P2(0) = ", coeficientes[2]+interpolaNewton(A,x,coeficientes))