#Autor: Lucas gabriel dos Santos Lima
#Data: 05-05-2024
#Objetivo: Criar um programa que leia uma medida em metros e a converta  para centímetros e milímetros

#Definição de variáveis    m = Medida  c = Centímetros     mi = Milímetros

m = float(input('Medida em metros a ser convertida: '))   #Recebe informações pelo teclado

c = m * 100    #Conversão de medidas para centímetros
mi = m * 1000   #Conversão de medidas para milímetros

print('{} Metros equivalem a {} centímetros e {} milímetros'.format(m,c,mi))    #Exibe informações na tela