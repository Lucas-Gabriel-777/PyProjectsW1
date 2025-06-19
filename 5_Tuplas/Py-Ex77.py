#Autor: Lucas Gabriel dos Santos Lima
#Data: 19-06-2025
#Objetivo: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

print('-'*73)
print(f'{"                      Contador de Vogais"}')
print('-'*73)
lista = (
    'Leao', "Macaco", "Pedreiro", "Jire", "Pneumatico", "Estriptococos", "Pneumatoforo", "carangueijo", "Mangue", 
    "Sirigueijo", "Omniman"
    )

for palavra in lista:
    print(f"As vogais da palavra {palavra} são: ", end = "")
    c = 0
    for letra in palavra.lower():
        if letra in 'aeiou':
            c +=1
            print(letra, end = ",")
    print(f" totalizando {c} vogais.")

print('-'*73)