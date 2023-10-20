import numpy as np
import matplotlib.pyplot as plt

x = np.array([
    [9.0],
    [0.5],
    [3.1],
    [5.8]
])

y = np.array([
    [0.4],
    [1.1],
    [4.4],
    [4.0]
])

# H(t) = ln(i(t)/t)
# a = ln(A)
# b = -B
# H(t)

Ht = np.log(y/x)

X = np.concatenate((np.ones_like(x), x), 1)

c = np.copy(Ht)

XTX = np.transpose(X)@X # transposta de X multiplicada por x

XTc = np.transpose(X)@c # transposta de X multiplicado por c

ac = np.linalg.solve(XTX, XTc) # a 'chapeu'
# ou ac1 = np.linalg.inv(XTX)@XTc

print(ac)

a = np.log(ac[0])
b = ac[1]

VE = c - X@ac # vetor de erros
EQ = np.sum(VE**2)
print(VE)
print(EQ)

xg = np.linspace(0, 10, 100)
yg = ac[0,0]+ ac[1,0]*xg
plt.plot(xg, yg)
plt.plot(x, y, "o")
plt.show()