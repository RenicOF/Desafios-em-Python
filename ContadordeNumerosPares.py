# Crie uma função que percorre uma lista de números e conta quantos são pares. Isso vai te ajudar a revisar laços e condicionais.


numeros = (1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 9, 10, 11, 12, 12)

def pares(numeros):
    contador = 0  # Inicializa o contador de números pares

    # Laço para verificar cada número na lista
    for n in numeros:
        # Verifica se o número é par
        if n % 2 == 0:
            contador += 1  # Incrementa o contador se o número for par
    
    return contador

resultado = pares(numeros)
print(f"Quantidade de números pares: {resultado}") 
