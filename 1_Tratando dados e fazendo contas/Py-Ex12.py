#Autor: Lucas Gabriel dos Santos Lima
#Data: 16-07-2024
#Objetivo: Crie um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Calculadora de descontos (5%)')
#O objetivo inicial seria realizar o cálculo com 5% de desconto, mas para tornar o programa mais versátil
#é adicionada uma variavel desconto (linha 14) ao código para que o calculo possa ser realizado
#considerando qualquer valor de desconto, para ativar essa funcionalidade, remova os símbolos "#" (hashtag)
#das linhas 14, 18 e 22 e adicione às linhas 19 e 23 como nos exemplos a seguir:

#p = p - ((15/100) * p)          #print ('O preço do produto com 15% de desconto é de {} R$'.format(p))

#Definição de variáveis e seus valores#
#d = float(input('Valor do desconto: '))#
p = float(input('Preço do produto: '))

#Cálculo de preço final,
#p =  p - ((d/100) * p)
p = p - ((15 / 100) * p)

#Exibindo valores
#print ('O preço do produto com {}% de desconto é de {} R$'.format(d,p))
print('O preço do produto com 15% de desconto é de {} R$'.format(p))