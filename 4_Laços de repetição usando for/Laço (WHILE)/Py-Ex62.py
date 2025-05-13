#Autor: Lucas Gabriel dos Santos Lima
#Data: 13-05-2025
#Objetivo: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. 
# Mostrando os 10 primeiros termos da progressão usando a estrutura while, 
# perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa deve ser encerrado quando ele disser que não.

print("Progressão Aritmética")

while True:
    print("\n")
    a = int(input("Primeiro termo da PA: "))
    razao = int(input("Razão: "))
    quantidade = int(input("Quantos termos você quer ver? (0 para cancelar): "))

    if  quantidade <0:
        while quantidade <0:
            print("\nOpção inválida, tente novamente ")
            quantidade = int(input("Quantos termos você quer ver? (0 para cancelar): "))
    elif quantidade == 0:
        break

    contador = 1
    while contador <= quantidade:
        termo = a + (contador-1) *razao
        print(termo,end = "")
        print(" - " if contador < quantidade else ".", end = "")
        contador += 1
    
