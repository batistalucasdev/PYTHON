def calcular_tempo_para_dobrar(deposito_inicial, taxa_juros):
    anos = 0
    valor_atual = deposito_inicial
    while valor_atual < 2 * deposito_inicial:
        valor_atual += valor_atual * (taxa_juros / 100)
        anos += 1
    return anos

def main():
    deposito_inicial = float(input("Digite o valor do depósito inicial: "))
    taxa_juros = float(input("Digite a taxa de juros ao ano (em %): "))
    
    anos = calcular_tempo_para_dobrar(deposito_inicial, taxa_juros)
    print(f"O valor acumulado será o dobro do valor inicial em {anos} anos.")

if __name__ == "__main__":
    main()
