#Descrição: Estão abertas as inscrições no Torneio Nacional de Peteca. Os jogadores podem competir, e para isso, basta se inscrever em uma das seguintes categorias: mirim (de quatro a sete anos), infantil (de oito a onze anos), juvenil (de doze a quinze anos), adulto (de dezesseis até quarenta e cinco anos), master (de quarenta e cinco anos até sessenta anos). Faça um programa que possibilite um jogador se inscrever no Torneio. O programa deve receber a idade e deve retornar uma frase dizendo em qual categoria foi inscrito.
#Entradas: idade, em anos
#Saídas: uma das seguintes palavras: “mirim”, “infantil”, “juvenil”, “adulto”, “master”, “fora da faixa etaria do torneio”. 

idade = int(input())

if (idade >=4 and idade <=7):
    print("mirim")
elif (idade >=8 and idade <= 11):
    print("infantil")
elif (idade >= 12 and idade <= 15):
    print("juvenil")
elif (idade >= 16 and idade <= 45):
    print("adulto")
elif (idade >= 45 and idade <= 65):
    print("master")
else:
    print("fora da faixa etaria do torneio")