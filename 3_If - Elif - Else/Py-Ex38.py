#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-04-2025
#Objetivo: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# – O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

n1 = int(input("Digite um número: "))
n2 = int(input("Mais um: "))

if n1>n2:
    print("O maior número é {}".format(n1))
elif n2>n1:
    print("O maior número é {}".format(n2))
else:
    print("Os valores são iguais")
