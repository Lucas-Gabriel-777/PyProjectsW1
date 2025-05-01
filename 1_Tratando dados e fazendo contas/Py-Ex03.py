#Autor: Lucas Gabriel
#Data.: 27-04-2024
#Objetivo: Crie um programa que leia dois números e mostre a soma entre eles

# Definição de variáveis     n1 = Primeiro Número    n2 = Segundo Número    SOMA = Soma dos dois números

n1 = int(input('Me dê um número: '))
n2 = int(input('Agora outro: '))

#Cálculo da soma
SOMA = n1+n2

#Exibe os valores na tela
print('A soma entre {} e {} é igual a {}.'.format(n1,n2,SOMA))
#✟