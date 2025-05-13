#Autor: Lucas Gabriel dos Santos Lima
#Data: 13-05-2025
#Objetivo: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# Mostrando os 10 primeiros termos da progressão usando a estrutura while.

a = int(input("Primeiro termo da PA: "))
razao = int(input("Razão: "))
contador = 1

while contador <= 10:
    termo = a + (contador-1) *razao
    print(termo,end = "")
    print(" - " if contador < 10 else ".", end = "")
    contador += 1