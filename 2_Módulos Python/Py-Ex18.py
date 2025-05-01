#Autor: Lucas Gabriel dos Santos Lima
#Data: 02-08-2024
#Objetivo: Crie um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# cosseno e tangente desse ângulo.

#Definição de variáveis    a = Ângulo      s = Seno      cos = Cosseno     tan= Tangente

#Importa a biblioteca "math"
import math
a = float(input('Ângulo a ser analisado: '))  #Recebe valor do Ângulo pelo teclado
s = math.sin(math.radians(a))   #Define o valor de seno pela função ".sin" importada da biblioteca math
cos = math.cos(math.radians(a))   #Define o valor de seno pela função ".cos" importada da biblioteca math
tan = math.tan(math.radians(a))   #Define o valor de seno pela função ".tan" importada da biblioteca math

#Exibe os resultados finais na tela
print('Analisando o ângulo {} temos {:.2f} para seno, {:.2f} para cosseno e {:.2f} para tangente'.format(a,s,cos,tan))
# ✟