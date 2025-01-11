# Questão 03

import json

# Carregar dados do JSON
with open("dados.json", "r") as arquivo:
    dados = json.load(arquivo)

# Filtrar dias com valor maior que zero
faturamentos = [dia["valor"] for dia in dados if dia["valor"] > 0]

# Cálculos
menor_faturamento = min(faturamentos)
maior_faturamento = max(faturamentos)
media_mensal = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media_mensal)

# Resultados
print(f"Menor faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias acima da média mensal: {dias_acima_da_media}")
