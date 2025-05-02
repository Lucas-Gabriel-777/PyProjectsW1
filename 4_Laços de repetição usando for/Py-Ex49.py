#Autor: Lucas Gabriel dos Santos Lima
#Data: 01-05-2025
#Objetivo: Criar um programa que leia um número pelo teclado e mostre a sua tabuada utilizando um laço for.

total = 0

num = int(input("Você deseja ver a tabuada de qual número? "))

for c in range (0,11):
    total = c * num
    print(" {} X {} = {}".format(c, num, total))