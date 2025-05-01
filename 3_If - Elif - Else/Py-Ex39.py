#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-04-2025
#Objetivo: Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input("Em que ano você nasceu? "))
ano_atual = date.today().year
idade = ano_atual - ano

if idade == 18:
    print("Você tem 18 anos, e caso ainda não tenha se alistado, é necessário que se aliste ainda esse ano")
elif idade<18:
    tempo = 18-idade
    print("Você ainda não precisa se alistar, mas precisará fazer isso em {} ano/s".format(tempo))
else:
    print("Você não precisa mais se alistar, porém, caso não tenha feito isso aos 18 anos, procure" \
    " uma unidade da junta militar para verificar se sua situação precisa ser regularizada")