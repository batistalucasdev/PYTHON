def ler_faturamento():
    faturamento = []
    for mes in range(12):
        valor = float(input(f"Digite o faturamento do mês {mes + 1}: "))
        faturamento.append(valor)
    return faturamento

def calcular_total_anual(faturamento_anual):
    return sum(faturamento_anual)

def calcular_total_filiais(faturamento_ano):
    total = 0
    for filial in faturamento_ano:
        total += calcular_total_anual(filial)
    return total

def calcular_total_periodo(faturamento_periodo):
    total = 0
    for ano in faturamento_periodo:
        total += calcular_total_filiais(ano)
    return total

def mostrar_dados(faturamento_periodo, anos):
    total_periodo = 0
    filiais = len(faturamento_periodo[0])
    for ano_idx, faturamento_ano in enumerate(faturamento_periodo):
        print(f"Dados do ano {anos[ano_idx]}:")
        total_ano = 0
        for filial_idx, faturamento_filial in enumerate(faturamento_ano):
            print(f"Filial {filial_idx + 1}:")
            for mes_idx, valor in enumerate(faturamento_filial):
                print(f"{anos[ano_idx]};Filial {filial_idx + 1};Mês {mes_idx + 1};{valor}")
            total_filial = calcular_total_anual(faturamento_filial)
            print(f"TOTAL {anos[ano_idx]} FILIAL {filial_idx + 1};{total_filial}")
            total_ano += total_filial
        print(f"TOTAL {anos[ano_idx]} TODAS FILIAIS;{total_ano}")
        total_periodo += total_ano
    print(f"TOTAL PERÍODO TODAS FILIAIS;{total_periodo}")

def main():
    anos = [2014, 2015, 2016, 2017]
    filiais = 3
    faturamento_periodo = []

    for ano in anos:
        faturamento_ano = []
        for filial in range(filiais):
            print(f"Lendo faturamento do ano {ano} para a filial {filial + 1}")
            faturamento_filial = ler_faturamento()
            faturamento_ano.append(faturamento_filial)
        faturamento_periodo.append(faturamento_ano)

    mostrar_dados(faturamento_periodo, anos)

if __name__ == "__main__":
    main()
