#Autor: Lucas Gabriel dos Santos Lima
#Data: 04-09-2024
#Objetivo: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

#Definição de variáveis      n = Número     u = Unidade    d = Dezena     c = Centena     m = Milhar

n = int(input("Me dê um número entre 0 e 9999: "))

while (n<0 or n >9999) :
    n = int(input("Me dê um número entre 0 e 9999: "))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(m))