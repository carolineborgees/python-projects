# Você vai construir um script que resolve um problema real de franquias — que é exatamente o seu contexto de trabalho.
# Contexto: você recebe uma lista de transações de franquias. Cada transação é um dicionário. Sua missão:

# Calcular o total de vendas por franquia
# Identificar qual franquia vendeu mais
# Imprimir um relatório simples no terminal

transacoes = [
    {"franquia": "Unidade Centro",  "valor": 4500.0},
    {"franquia": "Unidade Norte",   "valor": 3200.0},
    {"franquia": "Unidade Centro",  "valor": 6100.0},
    {"franquia": "Unidade Sul",     "valor": 8900.0},
    {"franquia": "Unidade Norte",   "valor": 4100.0},
    {"franquia": "Unidade Sul",     "valor": 2300.0},
    {"franquia": "Unidade Centro",  "valor": 1800.0},
]

# Seu código aqui:
# 1. Crie um dicionário chamado `vendas_por_franquia`

soma_por_franquia = {}

# 2. Itere sobre `transacoes` e some os valores por franquia
for transacao in transacoes:
    if transacao["franquia"] in soma_por_franquia:
        soma_por_franquia[transacao["franquia"]] += transacao["valor"]
    else:
        soma_por_franquia[transacao["franquia"]] = transacao["valor"]

print (soma_por_franquia)

# 3. Encontre a franquia com maior total (dica: função max())

maior_valor= max(soma_por_franquia.values())
print (maior_valor)

for franquia in soma_por_franquia:
    if soma_por_franquia[franquia] == maior_valor:
        nome_franquia = franquia


# 4. Imprima: "Franquia top: X com R$ Y em vendas"

print (f'Franquia top: {nome_franquia} com R$ {maior_valor} em vendas ')