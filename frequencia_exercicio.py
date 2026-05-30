# Contar frequência com dicionário
materias = ['Matematica', 'Ciencia', 'Geografia', 'Ciencia', 'Ciencia', 'Historia']

contagem = {}  # dicionário vazio

for materia in materias:
    if materia in contagem:
        contagem[materia] += 1   # já existe: incrementa
    else:
        contagem[materia] = 1    # não existe: cria com valor 1

print(contagem)
# {'Matematica': 1, 'Ciencia': 3, 'Geografia': 1, 'Historia': 1}
    