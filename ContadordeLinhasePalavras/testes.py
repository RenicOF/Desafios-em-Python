#Crie um programa que leia um arquivo .txt e conte quantas linhas e palavras existem no texto.

def contar_linhas_e_palavras(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        linhas = arquivo.readlines()  # Lê todas as linhas e armazena em uma lista
    
    # Contando linhas e palavras
    total_linhas = len(linhas)
    total_palavras = sum(len(linha.split()) for linha in linhas)  # Conta palavras dividindo cada linha
    
    return total_linhas, total_palavras

# Chamando a função e exibindo o resultado
resultado_linhas, resultado_palavras = contar_linhas_e_palavras("arquivos/tenho que aprender.txt")
print(f"Linhas: {resultado_linhas}")
print(f"Palavras: {resultado_palavras}")