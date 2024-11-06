# Tente criar uma calculadora simples que faça operações básicas como soma, subtração, multiplicação e divisão com base na entrada do usuário.

print("Essa é uma calculadora básica com soma, subtração, multiplicação e divisão")
operacao = int(input("Escolha qual operação irá fazer: digite 1 para Soma, 2 para Subtração, 3 para Multiplicação, ou 4 para Divisão: "))

if operacao == 1: 
    numero1 = int(input("Qual número deseja somar: "))
    numero2 = int(input("Qual o outro número que deseja somar: "))
    print("Resultado da soma:", numero1 + numero2)

elif operacao == 2:
    numero1 = int(input("Qual número deseja subtrair: "))
    numero2 = int(input("Qual o outro número que deseja subtrair: "))
    print("Resultado da subtração:", numero1 - numero2)

elif operacao == 3:
    numero1 = int(input("Qual número deseja multiplicar: "))
    numero2 = int(input("Qual o outro número que deseja multiplicar: "))
    print("Resultado da multiplicação:", numero1 * numero2)

elif operacao == 4:
    numero1 = int(input("Qual número deseja dividir: "))
    numero2 = int(input("Qual o outro número que deseja dividir: "))
    if numero2 != 0:  # Verifica se o divisor não é zero
        print("Resultado da divisão:", numero1 / numero2)
    else:
        print("Erro: Divisão por zero não é permitida.")

else:
    print("Operação inválida")
