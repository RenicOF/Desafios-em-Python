# Crie uma função que receba uma lista de números e retorne a soma de todos os números pares dessa lista.

numeros = (1,2,3,4,4,5,6,6,7,7,8,9,9,10,11,12,12)

def contador (numeros):

    numerospares = 0

    for numero in numeros:
        if numero % 2 == 0:
            numerospares += numero
    return numerospares

resultado = contador(numeros)
print(resultado)        
