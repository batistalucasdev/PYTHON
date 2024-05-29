def determinar_data(dia1,mes1,ano1,dia2,mes2,ano2):
    if ano1 > ano2:
        return(f'{dia1}/{mes1}/{ano1}')
    elif ano2 > ano1:
        return(f'{dia2}/{mes2}/{ano2}')
    elif ano1 == ano2:
        if mes1 > mes2:
            return(f'{dia1}/{mes1}/{ano1}')
        elif mes2 > mes1:
            return(f'{dia2}/{mes2}/{ano2}')
        elif mes1 == mes2:
            if dia1 > dia2:
                return(f'{dia1}/{mes1}/{ano1}')
            elif dia2 > dia1:
                return(f'{dia2}/{mes2}/{ano2}')
            elif dia1 == dia2:
                return(f'{dia1}/{mes1}/{ano1}')

def main ():
    dia1=int(input())
    mes1=int(input())
    ano1=int(input())
    dia2=int(input())
    mes2=int(input())
    ano2=int(input())

    data=determinar_data(dia1,mes1,ano1,dia2,mes2,ano2)
    print(f'{data}')

if __name__ == '__main__':
    main()
