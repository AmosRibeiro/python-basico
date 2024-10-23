lista_precos = [100, 200, 500, 800, 1300, 2001]


def calculo_impostos(preco):
    if preco <= 2000:
        imposto_ir = 0.2 * preco
    else:
        imposto_ir = 0.3 * preco
    
    imposto_aab = 0.4 * preco
    imposto_xxx = 0.9 * preco
    
    imposto_total = imposto_ir + imposto_aab + imposto_xxx
    return imposto_total

for preco in lista_precos:
    imposto_calculado = calculo_impostos(preco)
    print(f"O imposto calculado é de R${round(imposto_calculado, 2)}.")
    
nova_lista = [444, 666, 2400, 1000, 2000]
    
for preco in nova_lista:
    imposto_calculado = calculo_impostos(preco)
    print(f"O imposto calculado é de R${round(imposto_calculado, 2)}.")