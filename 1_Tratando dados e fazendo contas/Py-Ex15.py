#Autor: Lucas Gabriel dos Santos Lima
#Data: 16-07-2024
#Objetivo: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
#e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

#Definição de variáveis     km = quilômetros percorridos     d = dias de aluguel   vt = Valor total

#"Título" do programa
print('CALCULADORA DE ALUGUEL DE CARROS')

#Obtendo valores para as variáveis
km = float(input('Por quantos quilômetros o carro rodou? '))
d = int(input('Por quantos dias o carro ficou alugado? '))

#Cálculo do preço final do aluguel
vt = (km*0.15) + (d*60)

#Exibindo valores finais
print('O valor total do aluguel foi de {:.2f} R$'.format(vt))
# ✟