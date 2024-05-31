def calcular_numero(numero):

    if numero % 3 == 0 and numero % 5 == 0:
        return 'FIZZBUZZ'
    elif numero % 3 == 0 and not numero % 5 == 0:
        return 'FIZZ'
    elif numero % 5 == 0 and not numero % 3 == 0:
        return 'BUZZ'
    else:
        return numero

def main():
    numero=int(input())

    resultado=calcular_numero(numero)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
