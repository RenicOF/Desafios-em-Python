# Escreva uma função que salva uma lista de nomes ou números em um arquivo de texto.

# Lista de nomes que você quer salvar no arquivo
lista = ["Marcos", "Rubens", "Bob", "Alex"]

# Função para salvar a lista em um arquivo
def conversor(lista):
    with open("nomes.txt", "w") as arquivo:  # Abre o arquivo no modo de escrita
        for nome in lista:  # Para cada nome na lista
            arquivo.write(nome + "\n")  # Escreve o nome e adiciona uma nova linha

# Chama a função para salvar a lista
conversor(lista)
