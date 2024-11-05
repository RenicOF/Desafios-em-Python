# Crie uma função que receba uma lista de números e retorne uma nova lista contendo apenas os números únicos (ou seja, sem repetições).

numeros = (1,2,3,4,4,5,6,6,7,7,8,9,9,10,11,12,12)

def contador(numeros):
    numerosunicos = []  # Lista para armazenar números únicos

    for numero in numeros:
        if numero not in numerosunicos:  # Verifica se o número ainda não está na lista
            numerosunicos.append(numero)  # Adiciona o número único à lista

    return numerosunicos

resultado = contador(numeros)
print(resultado)  # Deve exibir uma lista de números únicos

