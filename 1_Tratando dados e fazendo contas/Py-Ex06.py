#Autor: Lucas Gabriel
#Data.: 27-04-2024
#Objetivo:Criar um programa que leia um número e mostre o dobro, o triplo e a raiz quadrada desse número

#Definição de variáveis     num = Número    d = Dobro   t = Triplo     rq = Raiz quadrada

#Recebe um número pelo teclado
num = int(input('Me dê um número: '))

#Cálculo de valores das variáveis
d = num * 2
t = num * 3
rq = num ** (1/2)

#Exibe os resultados na tela
print('O dobro de {} é {}'.format(num,d))
print('O triplo é {}'.format(t))
print('E a raiz quadrada é {}'.format(rq))