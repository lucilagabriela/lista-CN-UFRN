import math

def f(x, y, z):
    return 4 * x * y / z

def g(y):
    return math.cos(y)

def ponto_medio(h, x0, y0, z0):
    # Calcula y(1.4) e z(1.4) usando o método do ponto médio
    steps = int(1.4 / h)
    x = x0
    y = y0
    z = z0
    
    for _ in range(steps):
        y_middle = y + (h / 2) * f(x, y, z)
        z_middle = z + (h / 2) * g(y)
        
        x += h
        y += h * f(x, y_middle, z_middle)
        z += h * g(y_middle)
    
    return y, z

# Condições iniciais
x0 = 1
y0 = 4
z0 = 2.7
h = 0.4

# Calcula y(1.4) e z(1.4)
y_14, z_14 = ponto_medio(h, x0, y0, z0)

# Calcula y(1.4) + z(1.4)
resultado = y_14 + z_14

print(f'O valor de y(1.4) é aproximadamente {y_14:.4f}')
print(f'O valor de z(1.4) é aproximadamente {z_14:.4f}')
print(f'O resultado de y(1.4) + z(1.4) é aproximadamente {resultado:.4f}')