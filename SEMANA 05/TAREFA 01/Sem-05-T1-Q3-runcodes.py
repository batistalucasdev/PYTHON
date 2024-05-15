def percentual(valor,porcentagem):
    return valor*(porcentagem/100)

v=float(input())
p=float(input())
preco_aumento=v+(v*p/100)
desconto=v-(v*p/100)
print(f'{preco_aumento:.2f}')
print(f'{desconto:.2f}')
