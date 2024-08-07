def validar(data):
    dia = data // 1000000
    mes = (data % 1000000) // 10000
    ano = data % 10000
    bissexto = (ano%4==0 and ano%100!=0) or (ano%400==0)
    mes_31_dias = 1, 3, 5, 7, 8, 10, 12
    mes_30_dias = 4, 6, 9, 11

    if mes >= 1 and mes <= 12:
        if mes == 2 and bissexto:
            return True if dia >= 1 and dia <= 29 else False
        elif mes == 2 and not bissexto:
            return True if dia >= 1 and dia <= 28 else False

        if mes in mes_30_dias:
            return True if dia >= 1 and dia <= 30 else False
        elif mes in mes_31_dias:
            return True if dia >= 1 and dia <= 31 else False
    else:
        return False
        
def main():
    data=int(input("Digite uma data no formato DDMMAAAA: "))
    
    resultado=validar(data)
    print(f'A data digitada é: {resultado}')

if __name__ == '__main__':
    main()
