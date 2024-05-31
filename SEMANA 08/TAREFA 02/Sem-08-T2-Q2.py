def calcular_numero(numero):

    if numero > 0 and numero < 100000:
        centena_milhar=numero//100000
        dezena_milhar=(numero//10000)%10
        milhar=(numero//1000)%10
        centena=(numero//100)%10
        dezena=(numero//10)%10
        unidade=numero%10
        return f'A soma dos dígitos do número é: {centena_milhar + dezena_milhar + milhar + centena + dezena + unidade}'
    else:
        return -1

def main():
    numero=int(input("Digite um número: "))

    resultado=calcular_numero(numero)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
