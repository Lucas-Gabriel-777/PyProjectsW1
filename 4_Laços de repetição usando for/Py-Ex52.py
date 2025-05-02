#Autor: Lucas Gabriel dos Santos Lima
#Data: 02-05-2025
#Objetivo: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

while True:
    numero = int(input("\nDigite um número ( ou 0 para encerrar): "))

    total = 0
    for c in range (1, numero+1):
        if numero % c == 0:
            total += 1

    if total == 0:
        break
    elif total == 2:
        print("O número {} é primo".format(numero))
    else:
        print("O número {} não é primo".format(numero))