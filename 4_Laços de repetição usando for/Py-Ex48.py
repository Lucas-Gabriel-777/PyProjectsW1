#Autor: Lucas Gabriel dos Santos Lima
#Data: 01-05-2025
#Objetivo: Faça um programa que calcule a soma entre todos os números que 
# são múltiplos de três e que se encontram no intervalo de 1 até 500.

total = 0
num = int(input("Somar números divisíveis por 3 no intervalo de 1 a:\n"))
for c in range (1, num):
    if c % 3 == 0:
        total += c
        print(c, end = " ")
print("\n \nA soma dos números múltiplos de 3 no intervalo de 1 a {} é igual a {}".format(num,total))