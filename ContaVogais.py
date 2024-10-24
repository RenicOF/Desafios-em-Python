# Crie uma função que receba uma string e conte quantas vogais (aeiou) existem nela.
vogais = ("aeiouAEIOU")

print("Escreva um texto:")
texto = input("") 

def contar_vogais(texto):
    contador = 0  # Inicializa o contador de vogais
    for letras in texto:  # Itera sobre cada vogais na lista
        if letras in vogais:  # Verifica se a vogais
            contador += 1  # Incrementa o contador se tive vogais
    return contador  # Retorna a quantidade de vogais

# Exemplo de uso da função
resultado = contar_vogais(texto)  # Chama a função e armazena o resultado
print(f"Vogais: {resultado}")  # Exibe a quantidade de vogais
