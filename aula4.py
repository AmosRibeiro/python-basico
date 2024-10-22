lista_produtos = ["tijolo", "andaime", "cimento"]

produto_procurado = input("Procure um produto: ")
produto_procurado = produto_procurado.lower()

if produto_procurado in lista_produtos:
    print("Produto no estoque")
else:
    print("Produto não encontrado")
