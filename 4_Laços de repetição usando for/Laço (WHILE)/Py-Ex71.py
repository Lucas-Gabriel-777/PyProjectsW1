#Autor: Lucas Gabriel dos Santos Lima
#Data: 15-06-2025
#Objetivo: Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. 
# OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

nota50 = nota20 = nota10 = nota1 = 0
valor = int(input("Qual valor você deseja sacar? "))
valor1 = valor

nota = 50
notas = 0
print(f"Voce optou por sacar {valor} R$, e isso te deixa com")
while True:
    if valor1 >= nota:
        valor1 -= nota
        notas += 1
    else:
        if notas > 0:
            print(f"{notas} nota(s) de {nota}")
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        notas = 0
        if valor == 0:
            break
