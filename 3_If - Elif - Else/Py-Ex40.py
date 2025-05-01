#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-04-2025
#Objetivo: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem 
# no final, de acordo com a média atingida: 
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
media = (nota1+nota2)/2

if (media < 5):
    print("Infelizmente sua nota foi de {:f} pontos, você ficou abaixo da média e foi reprovado, sinto muito!".format(media))
elif (media >5 and media <= 6.9):
    print("Infelizmente sua nota foi de {:f} pontos, você ficou abaixo da média, mas ainda pode tentar a recuperação, boa sorte!".format(media))
else:
    print("Meus parabéns, sua nota foi de {:f} pontos e você foi aprovado/a")