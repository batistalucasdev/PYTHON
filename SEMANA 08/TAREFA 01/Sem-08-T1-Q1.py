def calcular_idade(dia,mes,ano,dia_nasc,mes_nasc,ano_nasc):
    idade=ano-ano_nasc
    
    if mes < mes_nasc:
        idade-1
    elif mes == mes_nasc:
        if dia < dia_nasc:
            return idade-1
    return idade

def main ():
    dia=int(input("Digite o dia da data atual: "))
    mes=int(input("Digite o mês da data atual: "))
    ano=int(input("Digite o ano da data atual: "))
    dia_nasc=int(input("Digite o dia da data de nascimento: "))
    mes_nasc=int(input("Digite o mês da data de nascimento: "))
    ano_nasc=int(input("Digite o ano da data de nascimento: "))

    resultado=calcular_idade(dia,mes,ano,dia_nasc,mes_nasc,ano_nasc)
    print(f'Sua idade é: {resultado} anos')

if __name__ == '__main__':
    main()
