#Autor: Lucas Gabriel dos Santos Lima
#Data: 02-05-2025
#Objetivo: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. Exemplos de palíndromos:


print("Um palíndromo é uma palavra ou frase que, lido de trás para a frente mantém o mesmo significado e sonoridade" \
"por exemplo, (ARARA) e (SUBI NO ONIBUS)")

palavra = str(input("\nDigite qualquer coisa ou tecle P para encerrar: ")).lower().strip().replace(" ", "")

palavra2 = palavra[::-1]

if palavra == palavra2:
    print("O texto: {} é um palíndromo, pois lido de trás para frente se torna {}".format(palavra, palavra2))
else:
    print("O texto: {} não é um palíndromo, pois lido de trás para frente se torna {}".format(palavra, palavra2))

    