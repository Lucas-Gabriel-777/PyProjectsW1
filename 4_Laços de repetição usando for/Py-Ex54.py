#Autor: Lucas Gabriel dos Santos Lima
#Data: 02-05-2025
#Objetivo: Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maiores = menores = 0
data = date.today().year

for c in range (1,8):

    while True:
        ano = int(input("Ano de nascimento da {}ª pessoa: ".format(c)))
        if data - ano > 0 and data -ano < 130:
            break
        print("\nA estimativa máxima de vida do ser humano é de 130 anos, por favor insira uma data válida\n")
        
    if data - ano >= 18:
        maiores += 1
    else:
        menores += 1
print("Apenas {} pessoas da lista são maiores de 18 anos".format(maiores))
print("As outras {} são menores de idade".format(menores))