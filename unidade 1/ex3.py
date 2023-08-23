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