def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

def main():
    numeros = []
    entrada = input('Digite 100 números inteiros: ')
    numeros = [int(numero) for numero in entrada.split()]

    media = calcular_media(numeros)
    print(f'{media}')

if __name__ == "__main__":
    main()
