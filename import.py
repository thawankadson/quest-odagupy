import json

# Carregando os dados do arquivo json
with open('faturamento.json', 'r') as f:
    dados = json.load(f)

# Ignorando dias sem faturamento
faturamento = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

# Calculando o menor valor de faturamento
menor_faturamento = min(faturamento)

# Calculando o maior valor de faturamento
maior_faturamento = max(faturamento)

# Calculando a média mensal
media_mensal = sum(faturamento) / len(faturamento)

# Calculando o número de dias com faturamento superior à média
dias_acima_da_media = sum(f > media_mensal for f in faturamento)

# Exibindo os resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")