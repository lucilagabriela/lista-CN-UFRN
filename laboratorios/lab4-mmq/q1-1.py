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

c = np.copy(y)

X = np.concatenate((np.ones_like(x), x), 1)

XTX = np.transpose(X)@X # transposta de X multiplicada por x

XTc = np.transpose(X)@c # transposta de X multiplicado por c

ac = np.linalg.solve(XTX, XTc) # a 'chapeu'
# ou ac1 = np.linalg.inv(XTX)@XTc

a = ac[0] + ac[1]

VE = c - X@ac # vetor de erros
EQ = np.sum(VE**2)


soma = np.sum(a) + EQ
print(f'{soma:.4f}')