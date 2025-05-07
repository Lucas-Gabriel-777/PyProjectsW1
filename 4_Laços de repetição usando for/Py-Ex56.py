#Autor: Lucas Gabriel dos Santos Lima
#Data: 07-05-2025
#Objetivo: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho 
# e quantas mulheres têm menos de 20 anos.

media = mm20 = maior = 0 
# mm20 = mulheres menores de 20 anos
# hmv = homem mais velho

for c in range (1,5):
    nome = str(input("\nNome da {}ª pessoa: ".format(c)))
    idade = int(input("Idade da {}ª pessoa: ".format(c)))
    media += idade
    sexo = str(input("Sexo da {}ª pessoa (M / F):  ".format(c)))

    if sexo in 'Ff' and idade < 20:
        mm20 += 1
    elif sexo in 'Mm' and idade > maior:
        maior = idade 
        hmv = nome

media = media/4

print("\nA média de idade do grupo é {} anos".format(media))
print("O homem mais velho do grupo é o {}".format(hmv))
print("Há {} mulher(es) menor(es) de 20 anos no grupo".format(mm20))      