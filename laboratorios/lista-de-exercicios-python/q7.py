#Implemente um programa que receba uma quantidade indeterminada de números inteiros. Assumindo que serão digitados pelo menos dois números, o programa deve se encerrar quando for digitado o número 0. Após isto, devem ser impressos os dois maiores números digitados.

numeros = []

while (True):
    x = int(input())
    if x == 0:
        break
    numeros.append(x)

print(f"Maior: {max(numeros)}")
numeros.remove(max(numeros))
print(f"Segundo maior: {max(numeros)}")