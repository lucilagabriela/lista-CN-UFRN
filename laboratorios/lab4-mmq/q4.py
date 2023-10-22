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

Ht = np.log(y/x)

X = np.concatenate((np.ones_like(x), x), 1)

c = np.copy(Ht)

XTX = np.transpose(X)@X # transposta de X multiplicada por x

XTc = np.transpose(X)@c # transposta de X multiplicado por c

# AO FINAL, Os parâmetos a0 e a1 devem estar em um vetor coluna chamado a,
a = np.linalg.solve(XTX, XTc) # a 'chapeu'
# ou ac1 = np.linalg.inv(XTX)@XTc

A = (np.exp(a[0]),-a[1])

# enquanto que o erro quadrático deve estar na variável EQ:
VE = c - X@a # vetor de erros
EQ = np.sum(VE**2)

##  NÃO ALTERE O CÓDIGO ABAIXO, ele é usado para verificação.
soma = np.sum(A) + EQ
print(f'{soma:.4f}')
