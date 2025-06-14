#Autor: Lucas Gabriel dos Santos Lima
#Data: 14-06-2025
#Objetivo: Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

contador = soma = 0
resp = "S"
while resp != "N":
    num = int(input("Digite um número: "))

    soma += num
    contador +=1

    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

    resp = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if resp == "N":
        break
media = soma / contador
print("Você digitou {} números, a média entre eles é {}".format(contador, media))
print("Além disso, o maior número registrado foi {} e o menor foi {}".format(maior,menor))
