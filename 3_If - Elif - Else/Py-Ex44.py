#Autor: Lucas Gabriel dos Santos Lima
#Data: 01-05-2025
#Objetivo: Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal 
# – 3x ou mais no cartão: 20% de juros

preco = float(input("Qual é o preço do produto? "))
metodo = int(input("Selecione o método de pagamento \n1- Dinheiro/Cheque \n2-À vista - Cartão \n3-Parcelado - Cartão \nMétodo: "))

if metodo ==1:
    preco2 = preco - (preco*0.10)
    print("Para pagamentos à vista em dinheiro, a compra recebe um desconto de 10%, sendo assim, a o valor de {:.2f}R$ passa a ser de {:.2f}R$".format(preco,preco2))

elif metodo == 2:
    preco2 = preco - (preco*0.05) 
    print("Para pagamentos à vista em dinheiro, a compra recebe um desconto de 5%, sendo assim, a compra de {:.2f}R$ passa a custar {:.2f}R$".format(preco,preco2))

elif metodo == 3:
    while True:
        parcelas = int(input("Quantidade de parcelas: "))
        if parcelas >0:
            break
        print("O número de parcelas deve ser maior que 0")

    if parcelas <=2:
        print("Não há descontos para pagamentos parcelados em até 2X, o valor final  da compra é o valor inicial de {:.2f}R$".format(preco))
    else:
        preco2 = preco + (preco*0.20)
        print("Para pagamentos parcelados em mais de 2X no cartão, a compra recebe um acréscimo de 20%, sendo assim, a compra de {:.2f}R$ passa a custar {:.2f}R$".format(preco,preco2))