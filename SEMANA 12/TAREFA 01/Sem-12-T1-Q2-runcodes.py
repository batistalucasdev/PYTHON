def calcular_rendimento_poupanca(saldo, taxa_juros):
    return saldo * (1 + taxa_juros)

def calcular_preco_carro(preco, taxa_aumento):
    return preco * (1 + taxa_aumento)

def calcular_meses_para_compra(preco_carro, saldo_inicial, taxa_juros, taxa_aumento):
    meses = 0
    saldo = saldo_inicial

    while saldo < preco_carro:
        saldo = calcular_rendimento_poupanca(saldo, taxa_juros)
        preco_carro = calcular_preco_carro(preco_carro, taxa_aumento)
        meses += 1
    
    return meses

def main():
    preco_carro = float(input())
    saldo_inicial = 10000
    taxa_juros = 0.007
    taxa_aumento = 0.004

    meses = calcular_meses_para_compra(preco_carro, saldo_inicial, taxa_juros, taxa_aumento)

    print(f"{meses}")

if __name__ == "__main__":
    main()
