#Autor: Lucas Gabriel dos Santos Lima
#Data: 10-04-2025
#Objetivo: Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input("Digite um numero inteiro: "))

print("Para qual representação voce deseja converter esse número? \n1-Binario    \n2-Octal   \n3-Hexadecimal \n")
opcao = int(input("Opcao"))
if opcao==1:
    print("O numero {} equivale a {} em Binario".format(num,bin(num)[2:]))
elif opcao ==2:
    print("O numero {} equivale a {} em Octal".format(num,oct(num)[2:]))
elif opcao ==3:
    print("O numero {} equivale a {} em Binario".format(num,hex(num)[2:]))
else:
    print("Opcao inválida!")