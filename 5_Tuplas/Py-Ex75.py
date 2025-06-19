#Autor: Lucas Gabriel dos Santos Lima
#Data: 17-06-2025
#Objetivo: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

lista = ()
for c in range (0,4):
    num = int(input("Digite um número inteiro: "))
    lista += (num,)
print(f"O número 9 apareceu {lista.count(9)} vezes")
if 3 in lista:
    print(f"O número 3 apareceu pela primeira vez na posição {lista.index(1)+1}")
print("\nOs números pares digitados foram: ", end = "")
for c in lista:
    if c % 2 == 0:
        print(c,end = "")