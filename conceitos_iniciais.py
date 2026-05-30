# Lista — mutável
frutas = ["maçã", "banana", "uva"]
frutas.append("manga")  # funciona

print(frutas)

# Tupla — imutável
coordenadas = (-23.5505, -46.6333)  # São Paulo
# coordenadas[0] = 0  # isso quebraria o código

# Dicionário — chave: valor
franquia = {
    "nome": "Unidade Centro",
    "cidade": "São Paulo",
    "vendas": 128500.0
}

print(franquia["nome"])    # "Unidade Centro"
print(franquia["vendas"])  # 128500.0