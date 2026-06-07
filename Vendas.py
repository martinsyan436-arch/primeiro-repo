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
