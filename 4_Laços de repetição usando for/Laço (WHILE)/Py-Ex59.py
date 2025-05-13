#Autor: Lucas Gabriel dos Santos Lima
#Data: 07-05-2025
#Objetivo: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

opcao = 0

print("CALCULADORA\n")
a = int(input("Digite um número: "))
b = int(input("Digite um número: "))
while opcao != 5:
    
    opcao = int(input("\n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa\nOpção: "))
    
    if 1 > opcao > 5:
        print("\nOpção inválida, use um valor entre 1 e 5")

    elif opcao == 1:
        soma = a + b
        print("\nO resultado da soma entre {} e {} é {}". format(a,b,soma))

    elif opcao == 2:
        mult = a * b
        print("\nO resultado da multiplicação entre {} e {} é {}". format(a,b,mult))

    elif opcao == 3:
        maior = a
        if b > a:
            maior = b
        print("\nO maior número entre {} e {} é {}". format(a,b,maior))
        
    elif opcao == 4:
        a = int(input("\nDigite um número: "))
        b = int(input("Digite um número: "))
    print("=-="*10)
    
