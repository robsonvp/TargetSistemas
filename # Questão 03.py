# Questão 03

import json

# Exemplo de dados em formato JSON
faturamento_json = '''
{
    "faturamento_diario": [1200.50, 1350.30, 0, 1800.75, 0, 2100.10, 2500.90, 0, 1750.20, 2300.50]
}
'''

# Carregando os dados
dados = json.loads(faturamento_json)
faturamento = [dia for dia in dados["faturamento_diario"] if dia > 0]

# Cálculos
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)
media_mensal = sum(faturamento) / len(faturamento)
dias_acima_da_media = sum(1 for dia in faturamento if dia > media_mensal)

# Resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
