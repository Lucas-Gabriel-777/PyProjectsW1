#Autor: Lucas Gabriel dos Santos Lima
#Data: 03-08-2024
#Objetivo: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Crie um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

#Definição de variáveis   n1 =  Primeiro Número   n2 =  Segundo Número  n3 = Terceiro Número   n4 = Quarto Número

#Importa a biblioteca random
import random

#Recebe valores para as variáveis pelo teclado
n1 = input('Primeiro(a) aluno(a): ')
n2 = input('Segundo(a) aluno(a): ')
n3 = input('Terceiro(a) aluno(a): ')
n4 = input('Quarto(a) aluno(a): ')
lista = [n1, n2, n3, n4]  # []Usado para criar uma lista com os elementos separados por vírgula

#random.choice(lista) = Faz escolha aleatória de elemento de lista referenciada entre parênteses
print('O(A) escolhido(a) foi {}.'.format(random.choice(lista)))

# ✟