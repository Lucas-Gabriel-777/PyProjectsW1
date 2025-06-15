#Autor: Lucas Gabriel dos Santos Lima
#Data: 14-06-2025
#Objetivo: Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maiores = homens = mulheres = 0

while True:
    idade = int(input("\nDigite a idade: "))

    if idade > 18:
        maiores += 1

    sexo = " "
    while sexo not in "FM":
        sexo = str(input("Sexo[M/F]: ")).strip().upper()[0]
    if sexo == "M":
        homens += 1
    if sexo == "F" and idade < 20: 
        mulheres += 1

    resp = " "
    while resp not in "SN":
        resp = str(input("Deseja continuar[S/N]? ")).strip().upper()[0]
    if resp == "N":
        break

print(f"Ao todo, foram registradas {maiores} pessoas com mais de 18 anos")
print(f"{homens} homens, e {mulheres} mulheres com menos de 20 anos")