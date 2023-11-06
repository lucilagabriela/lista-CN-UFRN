#Descrição: Crie um programa que faça a conversão de temperatura da escala Celsius para a escala Fahrenheit, ou vice-versa. O usuário deverá passar o valor da temperatura, e em seguida digitar “F”(ou”f”) para converter para Fahrenheit, ou  “C”(ou”c”) para converter para Celsius.  A equação para conversão entre as escalar é: C/5 = (F – 32)/9, onde C representa a temperatura em Celsius e F em Fahrenheit.
#Entradas: valor real de uma temperatura seguido da letra F ou C (as letras também podem ser minúsculas).   
#Saídas:
#O valor da temperatura com duas casas decimais e sua escala (C ou F)​“escala nao identificada: nao foi possível realizar conversao da temperatura”, se o usuário digitou uma escala não cadastrada.

valorTemp = float(input())
temp = input()

if temp == 'F' or temp == 'f':
    paraCelsius = (5*(valorTemp-32))/9
    print(f'{paraCelsius:.2f}C')
elif temp == 'C' or temp == 'c':
    paraF = ((32/9)+(valorTemp/5))*9
    print(f'{paraF:.2f}F')
else:
    print("escala nao identificada: nao foi possível realizar conversao da temperatura")