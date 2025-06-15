#Autor: Lucas Gabriel dos Santos Lima
#Data: 14-06-2025
#Objetivo: Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.

while True:
    c = 0
    num = int(input("\nVocê deseja ver a tabuada de qual número?  "))
    if num <= 0:
        break
    print("-"*25,"\n  Tabuada do número {}".format(num))
    print("-"*25)

    while c <= 10:
        mult = num * c
        print("{} X {} = {}".format(num, c, mult))
        c +=1