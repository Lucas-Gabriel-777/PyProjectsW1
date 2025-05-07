#Autor: Lucas Gabriel dos Santos Lima
#Data: 07-05-2025
#Objetivo: Crie um programa para o computador “pensar” em um número entre 0 e 10. 
# O usuário deve tentar adivinhar até acertar, mostrando no final 
# quantos palpites foram necessários para vencer.

from random import randint
#mc = Machine Choice       hc = Human Choice

while True:
    mc = randint(0,10)
    contador = 0
    continuar = 'p'

    print("\nEu escolhi um número entre 0 e 10, você consegue adivinhar qual é?")
    hc = int(input("Palpite: "))

    while hc != mc:
        contador += 1
        if hc < mc:
            print("Sinto muito, você errou, tente um número maior!\n")
        else:
            print("Sinto muito, você errou, tente um número menor!\n")
        hc = int(input("Palpite: "))

    print("\nO número escolhido foi {}, voce precisou de {} tentativas antes de acertar!".format(mc,contador))
    
    continuar = str(input("Quer jogar outra vez? ")).strip()[0]

    if continuar in "Nn":
        break
    elif continuar not in "SsNn":
        print("\nOpção inválida, aceito apenas sim ou não\n")
        continuar = str(input("Quer jogar outra vez? ")).strip()[0]
        