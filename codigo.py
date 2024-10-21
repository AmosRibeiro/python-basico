print("Olá, mundo!")

faturamento = 1000
custo = 700

imposto = faturamento * 0.1

lucro = faturamento - custo - imposto

margem_lucro = lucro / faturamento

print("O faturamento foi de", faturamento)
print("O custo foi de", custo)
print("O lucro foi de", lucro)
print("A margem de lucro foi de", round(margem_lucro, 1))

mensagem = "O faturamento da loja foi legal"
email = "email@email.com"

teve_lucro = True