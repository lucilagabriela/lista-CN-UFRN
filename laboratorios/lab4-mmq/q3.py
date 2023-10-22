import numpy as np

##   Recebe os vetores A e b do sistema
##                                          
##   Não altere o código abaixo           
##    
n = int(input())
arrayX = [float(input()) for x in range(n)]
arrayY = [float(input()) for x in range(n)]
x = np.array(arrayX).reshape((n,1))
y = np.array(arrayY).reshape((n,1))

## A partir daqui, as matrizes x e y já estão definidas
## SEU PROGRAMA A PARTIR DAQUI

def fx(a0, a1, x):
    y = a0 * np.log(0.3*x) + a1 * np.exp(-x/3)
    return y

# SEU CÓDIGO AQUI

X0 = [np.log(0.3*x[i]) for i in range(n)]
X1 = [(np.exp(-x[i]/3)) for i in range(n)]

X = np.concatenate((X0,X1),axis=1)

XTX = np.transpose(X)@X

XTy = np.transpose(X)@y

a = np.linalg.solve(XTX, XTy)

# AO FINAL, Os parâmetos a0 e a1 devem estar em um vetor coluna chamado a,
# enquanto que o erro quadrático deve estar na variável EQ:

VE = X@a - y
EQ = np.sum(VE**2)

##  NÃO ALTERE O CÓDIGO ABAIXO, ele é usado para verificação.
soma = np.sum(a) + EQ
print(f'{soma:.4f}')
