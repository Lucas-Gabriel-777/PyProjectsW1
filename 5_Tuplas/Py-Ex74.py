#Autor: Lucas Gabriel dos Santos Lima
#Data: 17-06-2025
#Objetivo: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint
maior = menor = 0
tupla = ()
for c in range (0,5):
    num = randint(0,50)
    tupla += (num,)
    c += 1

print(f"a lista de números gerada aleatóriamente é :{tupla} \nO maior número gerado foi {max(tupla)} e o menor foi {min(tupla)}.")
