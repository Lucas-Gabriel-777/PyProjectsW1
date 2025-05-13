#Autor: Lucas Gabriel dos Santos Lima
#Data: 07-05-2025
#Objetivo: Crie um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

a = int(input("Digite um número: "))
c = a
mult = 1
while c > 0:
    print("{}".format(c), end = "")
    print(" X " if c > 1 else " = ",end= "")
    mult *= c
    c-=1
print(mult)