#Autor: Lucas Gabriel dos Santos Lima
#Data: 16-07-2024
#Objetivo: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

#Definição de variáveis     a = Aumento     s1 = Salário      ns = Novo Salário#
print("CALCULADORA DE AUMENTO SALARIAL")

#O calculo de 15% de aumento pode ser ajustado para outro valor removendo o sinal "#" (hashtag) das
# linhas 11,16 e 20, adicionando-os às linhas 17 e 21

#a = float(input('Qual será a porcentagem do aumento? '))
s1 = float(input("Salário do funcionário: "))

#Cálculo do salário com 15% de aumento ou outro valor dependendo do input do usuário após as alterações descritas
#nas linhas 8 e 9
#ns = ((a/100) * s1) + s1
ns = ((15/100) * s1) + s1

#Exibindo valores finais
#print("O salário do funcionário que antes valia {} R$, recebeu um aumento de {}% e agora vale {} R$".format(s1,a,ns))
print("O Salário do funcionário que antes valia {} R$, recebeu um aumento de 15% e agora vale {} R$".format(s1,ns))
# ✟