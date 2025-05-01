#Autor: Lucas Gabriel dos Santos Lima
#Data: 01-08-2024
#Objetivo: Criar um programa que leia um número Real qualquer pelo teclado
#e mostre na tela a sua porção Inteira.

n = float(input('Me dê um número: ')) #Obtém valores para as variáveis por input(teclado)
print('A porção inteira de {} é {:.0f}'.format(n,n)) #Exibe os valores na tela

                                        #OU

#Para teste do código abaixo, remova o símbolo '#' (hashtag) das linhas 14 a 16
#e adicione o mesmo símbolo às linhas 6 e 7 para torná-las comentários.

#import math
#n = float(input('Me dê um número: '))
#print('A porção inteira de {} é {}'.format(n,math.trunc(n)))
#✟