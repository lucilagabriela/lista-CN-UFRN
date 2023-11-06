def lagrange_interpolation(x, xi, yi):
    n = len(xi) - 1
    result = 0.0
    
    for i in range(n+1):
        term = yi[i]
        for j in range(n+1):
            if j != i:
                term = term * (x - xi[j]) / (xi[i] - xi[j])
        result += term
    
    return result

# Calcula o valor do polinômio interpolador de Lagrange em x=a
PdeA = lagrange_interpolation(a, x, y)