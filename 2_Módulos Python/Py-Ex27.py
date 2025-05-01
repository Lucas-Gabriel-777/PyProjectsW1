#Autor: Lucas Gabriel dos Santos Lima
#Data: 29-09-2024
#Objetivo: Criar um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
#nome separadamente.

nome = input("Digite um nome: ").upper().strip()
ns = nome.split()

print("Primeiro nome: {} \nÚtlimo nome: {}".format(ns[0],ns[-1]))