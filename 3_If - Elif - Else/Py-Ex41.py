#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-04-2025
#Objetivo: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento 
# de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER
from datetime import date
ano_nascimento = int(input("Ano de nascimento do atleta: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if (idade<0):
    print("Data inválida, é impossível que alguem tenha 0 anos ou menos")
elif (idade<=9):
    print("Atleta MIRIM")
elif (idade <= 14):
    print("Atleta INFANTIL")
elif (idade <= 19):
    print("Atleta JÚNIOR")
elif (idade <= 25):
    print("Atleta SÊNIOR")
else:
    print("Atleta MASTER")
