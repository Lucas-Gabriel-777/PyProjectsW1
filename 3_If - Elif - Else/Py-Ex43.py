#Autor: Lucas Gabriel dos Santos Lima
#Data: 01-05-2025
#Objetivo: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

altura = float(input("Qual é sua altura? "))
peso = float(input("Qual é o seu peso? "))
peso = int(peso)

imc = peso/(altura **2 )

if imc <0:
    print("Você provavelmente inseriu alguma informação falsa, não é possível ter um IMC menor que 0")
if imc <18.5:
    print("IMC: {:.f}.Você está abaixo do peso, alimente-se de forma saudável e procure ajuda médica imediatamente!".format(imc))
elif imc >=18.5 and imc < 25:
    print("IMC: {:.f}.Você está no peso ideal, continue assim!".format(imc))
elif imc >=25 and imc < 30:
    print("IMC: {:.f}.Você está com sobrepeso, tente se alimentar de forma saudável, praticar exercícios e procure ajuda médica!".format(imc))
elif imc >=30 and imc < 40:
    print("IMC: {:.f}.Seu estado de saúde é grave, tente se alimentar de forma saudável, praticar exercícios e procure ajuda médica!".format(imc))
else:
    print("IMC: {:.f}.Seu IMC aponta obesidade mórbida, procure ajuda especializada imediatamente, você está correndo risco de vida".format(imc))