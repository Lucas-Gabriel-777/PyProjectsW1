#Autor: Lucas Gabriel dos Santos Lima
#Data: 14-06-2025
#Objetivo: Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

soma = c = 0
while True: 
    num = int(input("Digite um número ou 999 para encerrar: "))
    if num == 999: 
        break
    c+=1
    soma += num
print("Você digitou {} números, a soma entre eles equivale a {}".format(c,soma))