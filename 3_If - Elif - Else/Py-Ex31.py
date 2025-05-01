#Autor: Lucas Gabriel dos Santos Lima
#Data: 10-04-2025
#Objetivo:  Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

#d = Distância
d = 0

while d <= 0:
    d = int(input("Quantos quilômetros você vai rodar durante a viagem? "))
if d <= 200:
    preço = d * 0.50
    print(
        "A sua viagem vai durar {} Km, o preço cobrado para viagens de até 200Km é de 0.50 R$ por Km, então o preço final da viagem é de {} R$".format(d, preço))
else:
    preço = d * 0.45
    print(
        "A sua viagem vai durar {} Km, o preço cobrado por Km é de 0.45 R$  par viagens acima de 200Km, então o preço final da viagem é de {} R$".format(
            d, preço))


# OUTRA ALTERNATIVA É CALCULAR POSSIBILIDADES EM UMA ÚNICA LINHA
# preço = d*0.50 if d<=200 else d*0.45
# print("O preço da viagem é de 0.50R$ para viagens de até 200km, acima disso o preço passa a ser de 0.45R$ por KM" \
# "Como a sua viagem é de {}Km, o preço final será {}R$".format(d, preço))