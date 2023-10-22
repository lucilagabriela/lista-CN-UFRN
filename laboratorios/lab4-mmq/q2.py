import numpy as np

## Recebe os vetores A e b do sistema
##                                          
## Não altere o código abaixo           
##    
n = int(input())
m = int(input())
arrayX = [float(input()) for x in range(m)]
arrayY = [float(input()) for x in range(m)]
x = np.array(arrayX).reshape((m,1))
y = np.array(arrayY).reshape((m,1))

## A partir daqui, as matrizes x e y já estão definidas
## SEU PROGRAMA A PARTIR DAQUI

C1 = np.ones((m,1))

for i in range(1,n+1):
  C = x**i
  C1 = np.concatenate((C1,C),axis=1)

X = C1

XTX = np.transpose(X)@X

XTy = np.transpose(X)@y

a = np.linalg.solve(XTX, XTy)

VE = X@a - y
EQ = np.sum(VE**2)

## NÃO ALTERE O CÓDIGO ABAIXO, ele é usado para verificação.
soma = np.sum(a) + EQ
print(f'{soma:.4f}')