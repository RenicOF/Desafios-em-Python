#Crie um programa que pergunte ao usuário quantas notas ele quer inserir. Receba cada nota, armazene em uma lista e, ao final, mostre a média das notas e a maior nota.

# Pergunta ao usuário quantas notas ele quer inserir
quantidade_notas = int(input("Quantas notas você quer inserir? "))

# Cria uma lista para armazenar as notas
notas = []

# Recebe cada nota e armazena na lista
for i in range(quantidade_notas):
    nota = float(input(f"Digite a nota {i + 1}: "))
    notas.append(nota)

# Calcula a média das notas
media = sum(notas) / quantidade_notas

# Encontra a maior nota
maior_nota = max(notas)

# Exibe a média e a maior nota
print(f"Média das notas: {media}")
print(f"Maior nota: {maior_nota}")

# Opcional: Salva as notas em um arquivo
with open("notas.txt", "w") as arquivo:
    for nota in notas:
        arquivo.write(f"{nota}\n")
    arquivo.write(f"\nMédia: {media}\nMaior nota: {maior_nota}\n")
