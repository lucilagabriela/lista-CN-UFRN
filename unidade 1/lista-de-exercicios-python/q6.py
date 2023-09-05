#Faça um programa que lê a idade de uma pessoa e diz se ela tem direito ao atendimento preferencial (>65 anos). A cada execução o programa informa: “Se deseja continuar digite 1, caso contrário digite 2”. Se for digitado 1 o programa continua, se 2 o programa para! Nesse problema, você vai usar repetição, mas você não sabe quantas vezes vai repetir. O programa então tem duas entradas, uma é a idade e a outra é a escolha se continua ou para. Assim você deve mudar um pouco a estrutura apresentada antes. Nesse problema você não vai ter um contador! A cada repetição você vai perguntar ao usuário se ele vai continuar. Se ele digitar 2, para, se digitar 1 continua! Assim, ao invés de usar a equação de contagem no fim da repetição, você vai usar um comando de leitura para perguntar se ele quer continuar. Veja como fica a estrutura no exemplo abaixo.

x = 1
while x == 1:
    idade = int(input())
    if idade > 65:
        print('preferencial')
    else:
        print('normal')
    x = int(input(""))