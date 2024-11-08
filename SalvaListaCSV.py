#Crie uma função que salva as informações de uma lista de dados em um arquivo CSV.


import csv

lista_dados = ["Nome", "Gabriel", "Idade", "17", "Tipo", "Natural", "Gosto", "Maçã"]

def salvar_em_csv(dados, nome_arquivo):
    # Abre o arquivo no modo escrita
    with open(nome_arquivo, "w", newline='') as arquivo:
        writer = csv.writer(arquivo)
        
        # Escreve a lista inteira como uma linha no CSV
        writer.writerow(dados)

# Chama a função e salva em "dados.csv"
salvar_em_csv(lista_dados, "dados.csv")
