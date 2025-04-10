#1 - Adicionar tarefa
#2 - Concluir tarefa
#3 - Ver tarefas
#4 - Sair

lista_tarefas = []

while True:
    escolhar = int(input("Adicionar tarefa[digite 1], Concluir tarefa[digite 2], Ver tarefas[digite 3], Sair[digite 4]: "))
    if  escolhar == 1:
        tarefa = input("Escrevar a tarefa que vc quer adicionar: ")
        lista_tarefas.append(tarefa)
        print(lista_tarefas)

    elif escolhar == 2:
        print(lista_tarefas)
        tarefaconcluida = input("Escrevar a tarefa que vc quer concluir: ")
        if tarefaconcluida in lista_tarefas:
            lista_tarefas.remove(tarefaconcluida)


    elif escolhar == 3:
        print(lista_tarefas)

    elif escolhar == 4:
        print("Saindo!!!")
        break

    else:
        print("Numero invalido!!!")
        break
