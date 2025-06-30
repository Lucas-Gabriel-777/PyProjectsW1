#Autor: Lucas Gabriel dos Santos Lima
#Data: 30-06-2025
#Objetivo: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
# Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
resp = ''
print("Criando uma lista de números únicos")
print('-'*30)
while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break
    if num in lista:
        print(f"\nO número {num} já está contido na lista, escolha um outro!")
    else:
        lista.append(num)
        
    resp = str(input("\nDeseja continuar [S/N]? ")).strip().upper()
    if resp == "N":
        break

print('-'*30)
print("Lista formada: ",lista)
print("Lista ordenada: ", sorted(lista))