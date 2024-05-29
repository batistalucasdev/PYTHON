def calcular_idade(dia,mes,ano,dia_nasc,mes_nasc,ano_nasc):
    idade=ano-ano_nasc
    
    if mes < mes_nasc:
        idade-1
    elif mes == mes_nasc:
        if dia < dia_nasc:
            return idade-1
    return idade

def main ():
    dia=int(input())
    mes=int(input())
    ano=int(input())
    dia_nasc=int(input())
    mes_nasc=int(input())
    ano_nasc=int(input())

    resultado=calcular_idade(dia,mes,ano,dia_nasc,mes_nasc,ano_nasc)
    print(resultado)

if __name__ == '__main__':
    main()
