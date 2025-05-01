#Autor: Lucas Gabriel
#Data.: 04-05-2024
#Objetivo: Criar um programa que leia as duas notas de um aluno e calcule a média

#Definição de variáveis   n1 = Primeiro Número   n2 = Segundo Número    m = Média

n1= float(input('Qual foi a primeira nota do aluno? '))  # Recebe informações pelo teclado
n2 = float(input('E qual foi a segunda nota? '))

m = (n1+n2) / 2    #Cálculo da média

print('A média das notas do(a) aluno(a) é {}'.format(m))  #Exibe informações na tela