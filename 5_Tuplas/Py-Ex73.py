#Autor: Lucas Gabriel dos Santos Lima
#Data: 17-06-2025
#Objetivo: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Botafogo.

brazileirao_2025 = (
    "Flamengo", "Cruzeiro", "Bragantino", "Palmeiras", "Bahia",
    "Fluminense", "Atlético-MG", "Botafogo", "Mirassol", "Corinthians",
    "Grêmio", "Ceará", "Vasco", "São Paulo", "Santos",
    "Vitória", "Internacional", "Fortaleza", "Juventude", "Sport"
)

print(f"Os 5 primeiros colocados do brasileirâo 2025 são: {brazileirao_2025[:5]}")
print(f"\nOs 4 últimos colocados  são: {brazileirao_2025[-4:]}")
print(f"\nApresentando todos os time em ordem alfabética {sorted(brazileirao_2025)}")
print("\nBotafogo está em {}º colocado.".format(brazileirao_2025.index("Botafogo")+1))