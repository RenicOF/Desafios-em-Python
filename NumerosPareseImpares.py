#Escreva uma função que recebe uma lista de números e devolva duas listas: uma com todos os números pares e outra com todos os ímpares.

numeros = [1, 1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 10, 11]

def separar_pares_impares(numeros):
    numeros_pares = []
    numeros_impares = []
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)

    return numeros_pares, numeros_impares

resultado = separar_pares_impares(numeros)
print("Pares:", resultado[0])
print("Ímpares:", resultado[1])
