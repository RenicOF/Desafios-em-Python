lista = [5, 6, 7, 9, 20, 30, 40, 40, 40, 39, 39, 20, 20]

def conta(lista, item):
    contador = 0

    for numero in lista:
        if numero == item:  # Verifica se o número atual é igual ao item que queremos contar
            contador += 1
    return contador

# Teste da função com um item específico
item_para_contar = 40
resultado = conta(lista, item_para_contar)
print(f"O item {item_para_contar} aparece {resultado} vezes na lista.")
