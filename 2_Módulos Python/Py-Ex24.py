#Autor: Lucas Gabriel dos Santos Lima
#Data: 04-09-2024
#Objetivo: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”

#Definição de variáveis      nc = Nome da cidade

nc = input("Em qual cidade você mora? ").strip()

ncdv = nc.upper().split()

if (ncdv[0] == "SANTO"):
    print("O nome da sua cidade começa com {}".format(ncdv[0]))
else:
    print("Encerrando programa")
