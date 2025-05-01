#Autor: Lucas Gabriel dos Santos Lima
#Data: 10-04-2025
#Objetivo:  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print("Comparador")

a = int(input("Digite um número: "))
b = int(input("Agora outro: "))
c = int(input("Mais um: "))

maior = a
menor = c

if b>c and b>maior: 
    maior = b
elif b<c and b<a:
    menor = b

if c>a and c>b:
    maior =c
elif a<c and a<b:
    menor = a

print("Entre {}, {} e {}, o maior número é {} e o menor é {}".format(a,b,c,maior,menor))