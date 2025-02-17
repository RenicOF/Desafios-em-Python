lista = []

while True:
    res = input("\n[a] Adicionar | [r] Remover | [i] Imprimir | [s] Sair: ").lower()

    if res == "a":
        add = input("Escreva o nome da sua tarefa: ")
        lista.append(add)

    elif res == "r":
        if lista:  # Verifica se há itens para remover
            try:
                rev = int(input("Índice da tarefa removida: "))
                if 0 <= rev < len(lista):  # Garante que o índice é válido
                    lista.pop(rev)
                else:
                    print("Índice inválido! Digite um número dentro do intervalo.")
            except ValueError:
                print("Erro: Digite um número válido!")
        else:
            print("A lista está vazia, nada para remover!")

    elif res == "i":
        if lista:
            print("\nTarefas:")
            for i, tarefa in enumerate(lista):
                print(f"[{i}] {tarefa}")
        else:
            print("A lista está vazia!")

    elif res == "s":  # Opção para sair
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida! Escolha entre [a], [r], [i] ou [s].")
