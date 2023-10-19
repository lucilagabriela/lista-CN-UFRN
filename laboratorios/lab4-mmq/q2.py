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

X = np.vander(x.flatten(), n+1, increasing=True)

coeficientes = np.linalg.lstsq(X, y, rcond=None)[0] # coeficientes dos mínimos quadrados

a = coeficientes.reshape((n+1, 1))

y_predito = X.dot(coeficientes)

erro_quadratico = np.sum((y - y_predito) ** 2)

EQ = erro_quadratico

## NÃO ALTERE O CÓDIGO ABAIXO, ele é usado para verificação.
soma = np.sum(a) + EQ
print(f'{soma:.4f}')