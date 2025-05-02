#Autor: Lucas Gabriel dos Santos Lima
#Data: 02-05-2025
#Objetivo: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# No final, mostre os 10 primeiros termos dessa progressão.

print("Vamos criar uma progressão aritmética")
numero = int(input("Qual será o primeiro termo? "))
razao = int(input("Qual será a razão da PA? "))
print(" ")
for c in range (1,11):
    termo = numero + (c-1) *razao
    print (termo, end = " -> ")
print("Acabou")