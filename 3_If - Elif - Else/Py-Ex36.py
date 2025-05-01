#Autor: Lucas Gabriel dos Santos Lima
#Data: 10-04-2025
#Objetivo:  Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#  A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print("Simulador de empréstimo")
valor = float(input("Qual é o valor da casa que você sonha em adquirir? "))
salario = float(input("Qual é o valor do seu salário? "))
tempo = int(input("Em quantos anos você deseja pagar toda a conta? "))

tempo = tempo*12
prestacao = valor/tempo

if prestacao > (salario*0.30):
    print("Sinto muito, seu salário de {}R$ é inferior ao valor das prestações do empréstimo,"
          "espere mais um pouco ou escolha pagar em um prazo maior!".format(salario))
else:
    print("Meus parabéns, você está autorizado a realizar o empréstimo requerido, felicidades com a casa nova!")