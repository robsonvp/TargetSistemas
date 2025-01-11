# Questão 05

def inverter_string(texto):
    invertida = ""
    for char in texto:
        invertida = char + invertida
    return invertida

# Teste
entrada = input("Digite uma string para inverter: ")
print(f"String invertida: {inverter_string(entrada)}")
