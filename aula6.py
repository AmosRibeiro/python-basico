
dic_produtos = {"tijolo": 16, "andaime": 20, "caixa d'agua": 200}

print(dic_produtos["andaime"])

dic_produtos["caixa d'agua"] = dic_produtos["caixa d'agua"] * 1.3
print(dic_produtos)

print(len(dic_produtos))

dic_produtos["telha"] = 19
print(dic_produtos)

# verifica se uma chave existe
if "iphone" in dic_produtos:
    print("Existe produto")
else:
    print("Não encontrado.")
    
# verifica se um valor existe no valor do dicionario
if 9000 in dic_produtos.values():
    print("Existe")
else: 
    print("Não existe.")
    
    
nome_produto = input("Nome do produto: ")
preco_produto = input("Preço do produto: ")

nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)