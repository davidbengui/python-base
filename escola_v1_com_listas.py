#!/usr/bin/env python3
"""Exibe relatorio de criancas por atividade.

Imprimir a lista de craincas agrupadas por salas
que frequentam cada uma das atividades
"""

__version__ ="0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolada"]

aulas_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aulas_musica = ["Erik", "Carlos", "Maria"]
aulas_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]


atividades = [
    ("Ingles", aulas_ingles),
    ("Musica", aulas_musica),
    ("Danca", aulas_danca),
]

for nome_atividade, atividade in atividades:
    print(f"Alunoas da Atividade {nome_atividade}\n")
    print("-" * 50)
    atividade_sala1 = []
    atividade_sala2 = []

    for aluno in atividade:
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)

    print(f"{nome_atividade} sala1 ", atividade_sala1)
    print(f"{nome_atividade} sala2", atividade_sala2)
    print("-" * 50)