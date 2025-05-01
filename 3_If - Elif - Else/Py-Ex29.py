#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-09-2024
#Objetivo: Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada Km acima do limite.

#vm = Velocidade Medida     cm = Cálculo de Multa

cm = vm = 0

while vm <=0:
    vm = int(input("Qual foi a velocidade registrada? "))
if (vm > 80):
    cm = (vm - 80) * 7
    print("Sinto muito, você excedeu o limite de velocidade de 80km/h e foi multado(a) em {} R$".format(cm))
else:
    print("Sua velocidade está abaixo de 80km/h, muito bem, continue assim!")