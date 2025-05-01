# Autor: Lucas Gabriel dos Santos Lima
# Data: 09-09-2024
# Objetivo: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome

nome = input("Digite seu nome: ").strip().upper()
if ("SILVA" in nome):
    print("Você é um Silva")
else:
    print("Você não é um Silva ")