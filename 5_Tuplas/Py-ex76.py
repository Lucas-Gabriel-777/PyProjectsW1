#Autor: Lucas Gabriel dos Santos Lima
#Data: 19-06-2025
#Objetivo: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. 
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

lista = (
    'Maniçoba', 15.90,
    'Motor de Geladeira', 250,
    'Repimboca de parafuseta', 37.80,
    'Carburador furado', 7.80,
    'Paraquedas rasgado', 77.60,
    'Açúcar', 5.40
)

print('-'*52)
print(f'{"         Mercado Loucura Loucura Loucura":^40}')
print('-'*52)

for c in range(0, len(lista), 2):
    produto = lista[c]
    preço = lista[c+1]
    print(f"Produto: {produto:.<23} / Preço:{preço:>6.2f} R$")
    
print('-'*52)