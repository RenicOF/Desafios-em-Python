# Crie uma função que receba uma lista de números e retorne a média dos números.

numeros = (1, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 9, 10, 11, 12, 12)

def calcular_media(numeros):
    denominador = len(numeros)  # Número de elementos
    if denominador != 0:  # Verifica se o denominador não é zero
        soma = sum(numeros)
        resultado = soma / denominador  # Calcula a média
        return resultado
    else:
        return "A lista está vazia, divisão por zero não é permitida."

resultado = calcular_media(numeros)
print(resultado)  # Deve imprimir a média dos números na lista
