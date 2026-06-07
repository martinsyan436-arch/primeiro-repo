# Projeto: Análise de Vendas

vendas = [1500, 2300, 1800, 3200, 2700, 1900]
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"]

total = sum(vendas)
media = total / len(vendas)

print("=== Análise de Vendas ===")
print("Total vendido:", total)
print("Média mensal:", media)

print("\n=== Vendas por Mês ===")
for i in range(len(meses)):
    print(meses[i], ":", vendas[i])
maior = max(vendas)
menor = min(vendas)
i_maior = vendas.index(maior)
i_menor = vendas.index(menor)

print("\n=== Destaques ===")
print("Maior venda:", meses[i_maior], "-", maior)
print("Menor venda:", meses[i_menor], "-", menor)

print("\n=== Comparação com a Média ===")
for i in range(len(meses)):
    if vendas[i] >= media:
        print(meses[i], ": ACIMA da média")
    else:
        print(meses[i], ": abaixo da média")
