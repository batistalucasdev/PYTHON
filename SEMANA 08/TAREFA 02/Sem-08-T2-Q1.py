def calcular_numero(numero):

    if numero % 2 == 0:
        return numero + 5
    else:
        return numero + 8

def main():
    numero=int(input("Digite o número: "))

    resultado=calcular_numero(numero)
    print(f'O resultado da operação é: {resultado}')

if __name__ == '__main__':
    main()
