def aplicar_aumento_salario(salario, mes):
    if mes == 3:
        salario *= 1.05
    return salario

def aplicar_juros_divida(divida):
    return divida * 1.15

def avancar_mes(mes, ano):
    mes += 1
    if mes > 12:
        mes = 1
        ano += 1
    return mes, ano

def simular_divida_vs_salario(salario, divida, mes_inicio, ano_inicio):
    mes = mes_inicio
    ano = ano_inicio

    while salario >= divida:
        salario = aplicar_aumento_salario(salario, mes)
        divida = aplicar_juros_divida(divida)
        mes, ano = avancar_mes(mes, ano)

    return mes, ano

def main():
    salario_inicial = float(input("Digite o valor do salário inicial de Pedro: "))
    divida_inicial = float(input("Digite o valor da dívida inicial de Pedro: "))
    mes_inicio = 10
    ano_inicio = 2016

    mes, ano = simular_divida_vs_salario(salario_inicial, divida_inicial, mes_inicio, ano_inicio)
    print(f"A dívida será superior ao salário em {mes}/{ano}.")

if __name__ == "__main__":
    main()
