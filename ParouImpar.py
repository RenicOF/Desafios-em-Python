# Escreva um programa que receba um número inteiro do usuário e informe se o número é par ou ímpar.

print("Escreva um numero:")
numero = input() 
numero_calculado = int(numero) % 2

if numero_calculado == 0:
    print("numero par")
else:
    print("numero ímpar")


