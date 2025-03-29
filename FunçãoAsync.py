import asyncio

async def soma(x, y):
    print("Tarefa 1 iniciada")
    await asyncio.sleep(2)  # Simula a espera
    print("Tarefa 1 concluída")
    return x + y

async def multiplica(x, y):
    print("Tarefa 2 iniciada")
    await asyncio.sleep(2)
    print("Tarefa 2 concluída")
    return x * y

async def criar_funcao(funcao, *args):
    print("Tarefa 3 iniciada")
    await asyncio.sleep(5)
    print("Tarefa 3 concluída")
    return await funcao(*args)  # Aguarda a execução da função chamada

async def main():
    resultado_soma = await soma(5, 10)
    print(f"Resultado da soma: {resultado_soma}")

    resultado_multiplica = await multiplica(2, 10)
    print(f"Resultado da multiplicação: {resultado_multiplica}")

    resultado_criar_soma = await criar_funcao(soma, 5, 10)
    print(f"Resultado da função criada (soma): {resultado_criar_soma}")

    resultado_criar_multiplica = await criar_funcao(multiplica, 2, 10)
    print(f"Resultado da função criada (multiplica): {resultado_criar_multiplica}")

# Chama a função main, que é o ponto de entrada para o código assíncrono
asyncio.run(main())
