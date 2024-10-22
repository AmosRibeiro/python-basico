#email = input("Escreva seu email: ")
#nome = input("Seu primeiro nome: ")

#print(nome, email)

#print(f"{nome}, verifique seu email: {email} que enviamos um link de confirmação.")



#vendas = [100, 50, 14, 20, 30, 700]

lista_produtos = ["iphone", "airpod", "ipad", "macbook"]

#produto_procurado = input("Pesquisar...")
#produto_procurado = produto_procurado.lower()

#print(produto_procurado in lista_produtos)

lista_produtos.append("apple watch")
print(lista_produtos)

lista_produtos.remove("apple watch")
print(lista_produtos)

lista_produtos.pop(0)
print(lista_produtos)

precos = [1000, 1500, 3500]
precos[0] = 6000

lista_produtos = ["iphone", "airpod", "ipad", "macbook", "iphone", "ipad"]

print(lista_produtos.count("iphone"))

lista_produtos.sort()
print(lista_produtos)