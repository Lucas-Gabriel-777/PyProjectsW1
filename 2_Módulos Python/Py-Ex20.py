#Autor: Lucas Gabriel dos Santos Lima
#Data: 03-08-2024
#Objetivo: O mesmo professor do desafio 19 quer sortear a ordem
#de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
#e mostre a ordem sorteada.

#Importa a  biblioteca random
import random

#Define valores para as variáveis pelo teclado
n1 = input('Primeiro(a) aluno(a): ')
n2 = input('segundo(a) aluno(a): ')
n3 = input('Terceiro(a) aluno(a): ')
n4 = input('Quarto(a) aluno(a): ')
lista = [n1,n2,n3,n4]   #Cria lista com os valores entre []

random.shuffle(lista)   #random.shuffle(lista) = Comando que embaralha os elementos da lista criada na linha 15

#Exibe os valores na tela
print('A ordem de apresentação será: {}'.format(lista))
#✟