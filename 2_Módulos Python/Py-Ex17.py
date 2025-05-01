#Autor: Lucas Gabriel dos Santos Lima
#Data: 02-08-2024
#Objetivo: Crie um programa que leia o comprimento do cateto oposto e do
# cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

#Definição de variáveis    co = cateto oposto   ca = cateto adjacente   h = hipotenusa
co = float(input(('Medida do cateto oposto (menor lado) do triângulo: ')))
ca = float(input('Medida do cateto adjacente (lado médio) do triângulo: '))

#Cálculo da hipotenusa
h = (ca**2 + co**2) ** (1/2)

#Exibe os valores na tela
print('Com base nas medidas fornecidas, a hipotenusa do triangulo mede {:.2f}'.format(h))

                                        #OU

#Para teste da versão de código abaixo, remova o símbolo '#' (hashtag) das linhas 26 a 30,
#e adicione o mesmo símbolo às linhas 7, 8, 11 e 14 para torná-las comentários.

#from math import hypot (linha 21): esse comando importa a ferramenta de cálculo de hipotenusa da biblioteca "math"
#o mesmo resultado poderia ser obtido apenas com (import math), porém esse comando importa a biblioteca toda
#e o comando "from", escolhe ferramentas específicas para evitar armazenamento desnecessário de todas as ferramentas
#de uma biblioteca

#from math import hypot
#co = float(input(('Medida do cateto oposto (menor lado) do triângulo: ')))
#ca = float(input('Medida do cateto adjacente (lado médio) do triângulo: '))
#h = math.hypot(co,ca)
#print('Com base nas medidas fornecidas, a hipotenusa do triangulo mede {:.2f}'.format(h))
# ✟