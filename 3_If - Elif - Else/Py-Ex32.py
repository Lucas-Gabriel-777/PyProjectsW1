#Autor: Lucas Gabriel dos Santos Lima
#Data: 10-04-2025
#Objetivo:  Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date
ano = int(input("Ano bissexto? Descubra agora, me diga qual ano voce quer analisar ou 0 para analisar o ano atual: "))
if ano ==0: ano = date.today().year
    
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("O ano {} é bissexto!".format(ano))

else: 
    print("O ano {} não é bissexto!".format(ano))