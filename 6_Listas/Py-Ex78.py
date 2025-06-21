#Autor: Lucas Gabriel dos Santos Lima
#Data: 21-06-2025
#Objetivo: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

lista = []
for c in range (0,5):
    lista.append(int(input("Digite um número: ")))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        elif lista[c] < menor:
            menor = lista[c]
    c += 1
print("-"*30)
print(f"O maior número recebido foi {max(lista)} nas posições: ", end = "")
for c, v in enumerate(lista):
    if v == maior:
        print(f"{c+1}", end = ". ")

print(f"\nE o menor foi {min(lista)} nas posições: ", end = "")
for c, v in enumerate(lista):
    if v == menor:
        print(f"{c+1}", end = ". ")