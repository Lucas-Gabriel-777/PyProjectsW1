#Autor: Lucas Gabriel dos Santos Lima
#Data: 14-06-2025
#Objetivo: Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas 
# que ele conquistou no final do jogo.

import random
mc = random.randint(0,5)
contador = 0
print("-"*25, "\n  Vamos Jogar par ou ímpar")
print("-"*25)
while True:
    mc = random.randint(0,5)
    op = ""
    while op not in "SsNn":
        op = str(input("Par ou Ímpar[P/I]? ")).strip().upper()[0]
    num = int(input("Escolha um número entre 1 e 5: "))
    resultado = (mc + num) % 2

    if op == "P" and resultado == 0:
        print("Meus parabéns, você venceu!\n")
        contador +=1
    elif op == "P" and resultado == 1:
        print("Sinto muito, você perdeu!")
        break
    elif op == "I" and resultado == 0:
        print("Sinto muito, você perdeu!")
        break
    elif op == "I" and resultado == 1:
        print("Meus parabéns, você venceu!\n")
        contador +=1
print("Você ganhou {} vezes, reinicie o programa para jogar outra vez!".format(contador))