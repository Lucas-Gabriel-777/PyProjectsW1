#Autor: Lucas Gabriel dos Santos Lima
#Data: 01-05-2025
#Objetivo: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

print("Números pares entre 1 e 50")

for c in range (1, 51):
    if c%2 == 0:
        print(c, end = " ")