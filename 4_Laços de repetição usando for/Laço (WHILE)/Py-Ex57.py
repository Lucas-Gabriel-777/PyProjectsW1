#Autor: Lucas Gabriel dos Santos Lima
#Data: 07-05-2025
#Objetivo: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

while True:
    sexo = str(input("\nSexo (M/F): "))
    if sexo in "MmFf":
        break
    print("Informação inválida, tente novamente!")
