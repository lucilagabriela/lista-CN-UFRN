#Descrição: crie um programa que imprima os números ímpares em um intervalo [A;B], onde A > 0, e B <100. O programa deve checar se o intervalo [A,B] é válido, solicitando quantas vezes forem necessárias, os valores para A, e B, até que o usuário passe valores válidos.
#Entradas: inteiros A, B e C, com A > 0, B < 100, e B > A. #Saídas:  deve imprimir todos os números ímpares em [A,B]




A = int(input())
B = int(input())

if A > 0 and B < 100 and B > A:
    for n in range(A, B, 2):
        print(n)
