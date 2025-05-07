#Autor: Lucas Gabriel dos Santos Lima
#Data: 02-05-2025
#Objetivo: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
 
for c in range (1,8):
    while True:
        peso = float(input("Qual é o seu peso? "))
        if c == 1:
            maior = peso
            menor = peso
        if 0 < peso < 400:
            if peso > maior:
                maior = peso
            elif peso < menor:
                menor = peso

            break
        print("Insira um valor de peso maior que 0 e menor que 400")
        
print("O maior peso registrado foi {:f} Kg, e o menor foi {:f} Kg".format(maior,menor))
