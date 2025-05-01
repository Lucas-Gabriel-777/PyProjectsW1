#Autor: Lucas gabriel dos Santos Lima
#Data: 05-05-2024
#Objetivo: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#e mostre quantos dólares ela pode comprar

#Defini~ção de variáveis        dr = Dinheiro em Reais   dd = Dineiro em Dólar

dr = float(input('Quanto você tem em dinheiro para converter? '))    #Recebe valor pelo teclado
#Preço do dólar em 13-05-2024: 5,16    , é possível atualizar o programa substituindo o valor "5,16" na linha 12
#pelo preço atual da moeda Dólar

#Conversão de Real para Dólar
dd = (dr // 5.16)

#Exibe o valor na tela
print('Com {} Reais você pode comprar {} Dólar(es)'.format(dr,dd))