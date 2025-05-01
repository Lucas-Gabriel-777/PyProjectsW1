#Autor: Lucas gabriel dos Santos Lima
#Data: 05-05-2024
#Objetivo: Criar um programa que leia um número pelo teclado e mostre a sua tabuada

#Definição de variáveis   n = Número   c = Contador    m = Multiplicador

n = int(input('Número para cálculo de tabuada: ')) # Recebe valor pelo teclado

c = m = 1    #Variáveis são iniciadas com o valor "1"

while c <= 10:  #Enquanto o contador for menor que 10, faça:

    m = n * c  #Cálculo da tabuada
    print('{} X {} = {}'.format(n,c,m))  #Exibe a a linha da tabuada de acordo com o contador
    c+=1   #Incremento: Contador recebe contador + 1