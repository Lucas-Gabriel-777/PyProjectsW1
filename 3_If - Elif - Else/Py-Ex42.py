#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-04-2025
#Objetivo: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário 
# se elas podem ou não formar um triângulo e qual tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print("Quero formar um triângulo e preciso de três medidas, por favor, me ajude")
a = float(input("Medida da primeira reta: "))
b = float(input("Segunda reta: "))
c = float(input("terceria reta: "))

if a < b+c and b < a+c and c<a+b:
    print("Obrigado, medidas perfeitas para se formar um triângulo!")
    if a == b == c:
        print("O triângulo formado será um triângulo equilátero")
    elif a == b or a == c or b == c:
        print("O triângulo formado será um triângulo isósceles")
    else:
        print("O triângulo formado será um triângulo escaleno")
else:
    print("Infelizmente não é possível formar um triãngulo com essas medidas!")