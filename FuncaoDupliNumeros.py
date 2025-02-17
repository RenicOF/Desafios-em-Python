num1 = input("Escrevar o numero a ser duplica,tripicado ou quadrupicado: ")

def dupli():
    resultado = float(num1) * 2
    return resultado

def tipli():
    resultado = float(num1) * 3
    return resultado

def quadru():
    resultado = float(num1) * 4
    return resultado


print(dupli())
print(tipli())
print(quadru())
