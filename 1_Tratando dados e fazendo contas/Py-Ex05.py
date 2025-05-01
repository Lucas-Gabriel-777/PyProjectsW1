#Autor: Lucas Gabriel
#Data.: 27-04-2024
#Objetivo: Criar um programa que leia um número pelo teclado e mostre seu antecessor e seu sucessor

#Definição de variáveis       num = Número       a = Antecessor      s = Sucessor

num = int(input('Me dê um número: '))
a = num - 1
s = num + 1
print('O número {} tem {} como antecessor e {} como sucessor!'.format(num,a,s))