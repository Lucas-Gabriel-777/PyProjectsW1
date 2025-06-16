#Autor: Lucas Gabriel dos Santos Lima
#Data: 15-06-2025
#Objetivo: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

nota50 = nota20 = nota10 = nota1 = 0
valor = int(input("Qual valor você deseja sacar? "))
valor1 = valor

while valor > 0:
    if valor >= 50:
        while valor >=50:
            nota50 +=1
            valor -= 50
    elif valor >= 20:
        while valor >=20:
            nota20 +=1
            valor -= 20
    elif valor >= 10:
        while valor >=10:
            nota10 +=1
            valor -= 10
    elif valor >= 1:
        while valor >=1:
            nota1 +=1
            valor -= 1

print(f"\nVocê optou por sacar {valor1} R$, isso te deixa com")
if nota50 > 0:
    print(f"\n{nota50} nota(s) de 50", end=" ")
if nota20 > 0:
    print(f"\n{nota20} nota(s) de 20", end=" ")
if nota10 > 0:
    print(f"\n{nota10} nota(s) de 10", end=" ")
if nota1 > 0:
    print(f"\n{nota1} nota(s) de 1.")