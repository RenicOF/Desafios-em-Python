#Crie um script que leia um arquivo CSV com uma lista de produtos (nome, categoria, preço) e gere uma lista apenas dos produtos de uma categoria específica ou acima de um certo preço.

# Parâmetros de filtro
categoria_desejada = "Roupas"
preco_minimo = 100

# Lê o arquivo e filtra com base nos critérios
with open("nomes.txt", "r") as arquivo:
    linhas = arquivo.readlines()

    # Percorre cada linha e aplica o filtro
    for linha in linhas:
        # Divide cada linha por vírgulas para obter os campos
        nome, categoria, preco = linha.strip().split(", ")
        
        # Converte o preço para inteiro para comparação
        preco = int(preco)
        
        # Verifica se a linha corresponde ao filtro de categoria ou preço
        if categoria == categoria_desejada or preco >= preco_minimo:
            print(f"{nome}, {categoria}, {preco}")
