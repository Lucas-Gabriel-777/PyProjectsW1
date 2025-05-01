#Autor: Lucas Gabriel dos Santos Lima
#Data: 09-09-2024
#Objetivo: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = input("Digite qualquer coisa: ").strip().upper()
c = frase.count('A')
print("A letra 'A', aparece {} vezes na setença".format(c))
