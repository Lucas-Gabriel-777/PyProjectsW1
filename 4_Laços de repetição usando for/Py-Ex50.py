#Autor: Lucas Gabriel dos Santos Lima
#Data: 01-05-2025
#Objetivo: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. 
# Se o valor digitado for ímpar, desconsidere-o.

total = 0
lista = []

for c in range (1,7):
    numero = int(input("Digite o {}º número: ".format(c)))
    if numero % 2 == 0:
        total += numero
        lista.append(numero)
        
print("Os números pares que você digitou são {}".format(lista))
print("A soma dos números pares que voceê digitou resulta em {}".format(total))