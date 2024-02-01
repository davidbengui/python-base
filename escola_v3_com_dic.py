#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por salas
que frequentam cada uma das atividades
"""

__version__ = "0.1.0"

# Defina um dicionário para representar as salas e seus alunos
salas = {
    "sala1": ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2": ["Joao", "Antonio", "Carlos", "Maria", "Isolada"]
}

aulas_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aulas_musica = ["Erik", "Carlos", "Maria"]
aulas_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("Ingles", aulas_ingles),
    ("Musica", aulas_musica),
    ("Danca", aulas_danca),
]

# Crie um dicionário para armazenar as atividades por sala
atividades_por_sala = {sala: {atividade: set() for atividade, _ in atividades} for sala in salas}

# Preencha o dicionário com as crianças que participam de cada atividade em cada sala
for sala, alunos in salas.items():
    for nome_atividade, atividade in atividades:
        atividade_sala = set(alunos) & set(atividade)
        atividades_por_sala[sala][nome_atividade] = atividade_sala

# Imprima o relatório
for sala, atividades_sala in atividades_por_sala.items():
    print(f"Alunos da Sala {sala}\n")
    print("-" * 50)

    for nome_atividade, alunos in atividades_sala.items():
        print(f"Atividade {nome_atividade}: {alunos}")

    print()
    print("-" * 50)
