#Crie uma função que receba uma lista de números e retorne o maior e o menor número da lista.

lista_numeros = [1,2,3,4,5,6,7,8,9,10]

def contador(lista_numeros):
    # Inicialize maior e menor com o primeiro elemento da lista
    maior = lista_numeros[0]
    menor = lista_numeros[0]

    # Percorre cada número na lista
    for numeros in lista_numeros:
        # Verifica se o número é maior ou menor e atualiza as variáveis
        if numeros > maior:
            maior = numeros
        if numeros < menor:
            menor = numeros

    # Retorna maior e menor
    return maior, menor

resultado = contador(lista_numeros)   
print(resultado)
