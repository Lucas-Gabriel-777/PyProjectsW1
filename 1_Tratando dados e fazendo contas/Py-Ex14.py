#Autor: Lucas Gabriel dos Santos Lima
#Data: 16-07-2024
#Objetivo: Criar um programa que converta uma temperatura digitando em graus Celsius e
#converta para graus Fahrenheit.

#Definição de variáveis     c = Celsius     f = Fahrenheit

#"Título" do programa
print('CONVERSOR DE TEMPERATURA EM CELSIUS PARA FAHRENHEIT')

#Obtém valor a ser calculado
c = float(input('Qual é a temperatura em graus Celsius a ser convertida? '))

#Cálculo para conversão de temperatura
f = (c * 1.8) + 32

#Exibe resultado final
print('{} graus Celsius equivalem a {} graus Fahrenheit'.format(c,f))
# ✟