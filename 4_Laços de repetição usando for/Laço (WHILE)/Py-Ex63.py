#Autor: Lucas Gabriel dos Santos Lima
#Data: 13-05-2025
#Objetivo: Escreva um programa que leia um número N inteiro qualquer e mostre na tela 
# os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
# 0 – 1 – 1 – 2 – 3 – 5 – 8

quantidade = int(input("Quantos termos você deseja ver da sequência? "))
termo = 0
a = 1
b = 0
c = 0
while c <= quantidade:
    print (termo, "- " if c < quantidade else ".", end = "")
    b = a
    a = termo 
    termo = a + b
    c+=1