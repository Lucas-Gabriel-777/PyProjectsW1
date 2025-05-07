#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-09-2024
#Objetivo: Escreva um programa que faça o computador “pensar” em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
#mc = Machine Choice       hc = Human Choice

mc = randint(0,5)

print("Eu escolhi um número entre 0 e 5, você consegue adivinhar qual é?")
hc = int(input("Palpite: "))

while ( hc<0 or hc>5):
    hc = int(input("Opção inválida, digite um número entre 0 e 5. \nPalpite: "))
if (hc == mc):
    print("Parabéns, eu escolhi o número {} e você descobriu!".format(mc))
else:
    print("Sinto muito, o número que eu escolhi foi {}, você escolheu {} e errou!".format(mc,hc))