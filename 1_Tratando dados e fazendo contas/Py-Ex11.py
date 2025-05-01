#Autor: Lucas Gabriel dos Santos Lima
#Data: 16-07-2024
#Objetivo: Criar um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que
# cada litro de tinta pinta uma área de 2 metros quadrados.


#Definição de variáveis
altura = float(input('Qual é a altura da parede? '))
largura = float(input('E a largura? '))

#Cálculo de valores das variáveis
area = altura*largura
lt = area/2

#Exibição de valores finais
print('Serão necessários {} litros de tinta para pintar a parede'.format(lt))
# ✞