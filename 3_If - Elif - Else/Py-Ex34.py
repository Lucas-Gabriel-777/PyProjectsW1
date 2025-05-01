#Autor: Lucas Gabriel dos Santos Lima
#Data: 10-04-2025
#Objetivo:  Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Digite seu salário: "))
novo_salario = 0
aumento = 10
if 0> salario <= 1250.00:
    novo_salario+= salario + (salario* 0.10)
else:
    aumento = 15
    novo_salario+=salario + (salario*0.15)

print("O salario de {}R$ passa a ser de {}R$ com aumento de {} %".format(salario,novo_salario,aumento))