faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Calculando o faturamento total
total = sum(faturamento.values())

# Calculando o percentual de representação de cada estado
percentual = {estado: (faturamento / total) * 100 for estado, faturamento in faturamento.items()}

# Exibindo os resultados
for estado, perc in percentual.items():
    print(f"{estado}: {perc:.2f}%")