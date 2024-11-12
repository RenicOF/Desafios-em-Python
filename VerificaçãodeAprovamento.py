#Receba uma lista de dicionários com nome e nota de alunos e verifique se cada aluno passou, com base em uma média de aprovação de 6. Retorne uma lista com os nomes dos alunos aprovados.

notas_alunos = {
    "Kaike": "5, 6, 9, 8",
    "Laura": "4, 3, 5, 2",
    "Ana": "5, 7, 6, 4",
    "Orto": "6, 9, 9, 10",
    "Vale": "3, 5, 9, 8"
}

def verifica(notas_alunos):
    aprovados = []  # Lista para armazenar os nomes dos alunos aprovados
    for nome, notas_str in notas_alunos.items():
        # Converte a string de notas em uma lista de floats
        notas = list(map(float, notas_str.split(", ")))
        # Calcula a média das notas
        media = sum(notas) / len(notas)
        # Verifica se a média é igual ou superior a 6
        if media >= 6:
            aprovados.append(nome)
    return aprovados

resultado = verifica(notas_alunos)
print("Alunos aprovados:", resultado)
