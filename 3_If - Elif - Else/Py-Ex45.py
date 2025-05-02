#Autor: Lucas Gabriel dos Santos Lima
#Data: 01-05-2025
#Objetivo: Crie um programa que faça o computador jogar Jokenpô com você.

# em = Escolha da máquina     eh = Escolha de humano
# cvm = Contador de vitórias da máquina      cvh = Contador de vitórias do humano

import random 
cvm = cvh = eh = 0

opcoes = ["Papel", "Pedra", "Tesoura"]

print("JOKENPÔ")
while True:

    print("Vamos jogar Jokenpô \nEscolha uma opção para jogar ou tecle 0 para sair!")
    print("1 - PEDRA \n2 - PAPEL  \n3 - TESOURA")

    em = random.choice (opcoes)
    eh = int(input("Opção: "))

    if eh == 0:
        print("Obrigado por jogar, você ganhou {} vezes, e eu ganhei {} vezes".format(cvh,cvm))
        break

    if em == "Papel":
        if eh == 1:
            print("Escolhi Papel, você escolheu Papel e empatamos!")
        elif eh == 2:
            print("Escolhi Papel, você escolheu Pedra e perdeu, sinto muito!")
            cvm +=1
        elif eh ==3:
            print("Escolhi Papel, você escolheu tesoura e ganhou, meus parabéns!")
            cvh += 1
        else:
            print("Numero inválido, tente novamente com um número entre 1 e 3")

    elif em == "Pedra":
        if eh == 1:
            print("Escolhi Pedra, você escolheu Papel e ganhou, meus parabéns!")
            cvh += 1
        elif eh == 2:
            print("Escolhi Pedra, você escolheu Pedra e empatamos!")
        elif eh ==3:
            print("Escolhi Pedra, você escolheu tesoura e perdeu, sinto muito!")
            cvm += 1
        else:
            print("Numero inválido, tente novamente com um número entre 1 e 3")

    elif em == "Tesoura":
        if eh == 1:
            print("Escolhi Tesoura, você escolheu Papel e perdeu, sinto muito!")
            cvm +=1
        elif eh == 2:
            print("Escolhi Tesoura, você escolheu Pedra ganhou, meus parabéns!")
            cvh += 1
        elif eh ==3:
            print("Escolhi Tesoura, você escolheu Tesoura e empatamos!")
        else:
            print("Numero inválido, tente novamente com um número entre 1 e 3")
    print("\n")