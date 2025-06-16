#Autor: Lucas Gabriel dos Santos Lima
#Data: 15-06-2025
#Objetivo: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

print("-"*25, "\n  Lista de compras")
print("-"*25)

total = caro = menor = contador = 0
barato = " "

while True:
    nome = str(input("\nNome do produto: "))
    preço = float(input("Preço do produto: "))
    contador += 1
    total += preço
    if contador == 1 or preço < menor:
        menor = preço
        barato = nome
    if preço > 1000:
        caro += 1
    
    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if resp == "N":
        break

print(f"O valor total da compra é {total:10.2f} R$")
print(f"A lista possui {caro} produto(s) que custa(m) mais de 1.000,00 R$")
print(f"O produto mais barato da lista é {barato}")