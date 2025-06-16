#Autor: Lucas Gabriel dos Santos Lima
#Data: 16-06-2025
#Objetivo: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = ["zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove",
    "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete","dezoito", "dezenove", "vinte"]

num = int(input("Digite um número: "))
c = 0
while c <= num:
    print(f"{numeros[c]}", ", " if c < num else ".", end = "")
    c+=1