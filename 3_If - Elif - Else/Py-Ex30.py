#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-09-2024
#Objetivo: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

num = 0
while num <=0:
    num = int(input("Digite um número INTEIRO e MAIOR que 0: "))
if(num%2 == 1):
    print("Você escolheu o número {}, que é ímpar".format(num))
else:
    print("Você digitou o número {}, que é par".format(num))