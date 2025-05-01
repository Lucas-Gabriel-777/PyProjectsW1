#Autor: Lucas Gabriel dos Santos Lima
#Data: 10-04-2025
#Objetivo:  Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo.

print("Quero formar um triângulo e preciso de três medidas, por favor, me ajude")
a = float(input("Medida da primeira reta: "))
b = float(input("Segunda reta: "))
c = float(input("terceria reta: "))

if a < b+c and b < a+c and c<a+b:
    print("Obrigado, medidas perfeitas para se formar um triângulo!")
else:
    print("Infelizmente não é possível formar um triãngulo com essas medidas!")