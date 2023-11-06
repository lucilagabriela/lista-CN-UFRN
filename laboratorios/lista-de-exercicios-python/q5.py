#Implemente um programa que recebe 20 números inteiros positivos e os armazena em um vetor A. Em seguida o programa deve separar os números pares e ímpares em dois vetores de pares e ímpares. Os números pares e ímpares devem ser armazenados nos seus respectivos vetores.

A = []
vetPar = []
vetImpar = []
for i in range(20):
    x = int(input())
    A.append(x)
    if x % 2 == 0: # par
        vetPar.append(str(x))
    else:
        vetImpar.append(str(x))

print("Pares: " + ",".join(vetPar))
print("Impares: " + ",".join(vetImpar))