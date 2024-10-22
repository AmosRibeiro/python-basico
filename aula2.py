faturamento = 1200
custo = 700
lucro = faturamento - custo

print(f"Faturamento: {faturamento}, Custo: {custo}, Lucro: {lucro}")

email_cliente = "amos@email.com"

email_cliente = email_cliente.upper()
print(email_cliente)
email_cliente = email_cliente.lower()
print(email_cliente)

# encontrar "@" no email
print(email_cliente.find("@")) # -1 quando não encontrar

# tamanho do texto
print(len(email_cliente))

# pegar um caractere
print(email_cliente[0]) # pega o elemento do indice N entre os colchetes

print(email_cliente[-1]) 

# pegar um pedaço do texto
print(email_cliente[:4]) #até o indice 4

print(email_cliente[4:]) #do 4 pra frente 

# trocar um texto
novo_email = email_cliente.replace("email.com", "hotmail.com")
print(novo_email)

nome = "amos ribeiro"
print(nome.capitalize())
print(nome.title())

# pegar o servidor do email
posicao_arroba = email_cliente.find("@")
servidor = email_cliente[posicao_arroba:]
print(servidor)