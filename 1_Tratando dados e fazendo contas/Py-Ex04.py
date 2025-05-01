#Autor: Lucas Gabriel
#Data.: 27-04-2024
#Objetivo: Criar um programa que leia algo pelo teclado e mostre informações sobre o texto

tema = input('Digite qualquer coisa: ')  # Variáveil "tema" Recebe informações pelo teclado (input)


print('O texto digitado foi {} e sua classe primitiva é {}.'.format(tema, type(tema)))

print('É alfa-numérico:', tema.isalnum())  # "Variável.exemplo ": Comando usado para retornar algumas características do
print('É alfabético:', tema.isalpha())          # "objeto" refernciado antes de "."
print('Está em minúsculo:',tema.islower())
print('Está em maiúsculo:',tema.isupper())
print('É composto por espaços:',tema.isspace())
print('É decimal:',tema.isdecimal())