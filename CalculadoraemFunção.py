#Escreva uma função para cada operação matemática (soma, subtração, multiplicação e divisão). Em seguida, peça ao usuário para escolher uma operação e insira dois números, e use a função correspondente para retornar o resultado.

# Definindo uma função para cada operação
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    # Verifica se o divisor é diferente de zero para evitar divisão por zero
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

# Solicitando ao usuário que escolha uma operação
operacao = int(input("Calculadora de soma digite 1, subtração digite 2, multiplicação digite 3 e divisão digite 4:"))

# Solicitando ao usuário que insira dois números
numero1 = int(input("Qual seu primeiro número: "))
numero2 = int(input("Qual seu segundo número: "))

# Selecionando e executando a operação com base na escolha do usuário
if operacao == 1:
    print("Resultado da Soma:", soma(numero1, numero2))
elif operacao == 2:
    print("Resultado da Subtração:", subtracao(numero1, numero2))
elif operacao == 3:
    print("Resultado da Multiplicação:", multiplicacao(numero1, numero2))
elif operacao == 4:
    print("Resultado da Divisão:", divisao(numero1, numero2))
else:
    print("Operação inválida.")
