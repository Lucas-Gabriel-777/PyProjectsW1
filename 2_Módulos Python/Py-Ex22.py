#Autor: Lucas Gabriel dos Santos Lima
#Data: 03-08-2024
#Objetivo: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas,
#quantas letras no total (sem considerar espaços)
#quantas letras tem o primeiro nome

nome = input('Digite seu nome completo: ')    #Define valor para a variável nome pelo teclado
print(nome.upper())                           #Transforma a variável nome em caracteres maiúsculos

print('O seu nome tem {} letras'.format(len(nome.strip())))    #len(nome.strip()) : "len()" conta os carateres de "nome"
                                                               #strip() remove os espaços da variável nome
#variável "n" recebe nome com todas as palvras separadas

n = nome.split()    # .split() : divide os conjuntos "palavras", da variável "nome"
print(n[0])      #n[0] : Evidencia o elemento 0 da variável "n"

# ✟