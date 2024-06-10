def calcular_media():
    numeros = []
    for i in range(100):
        numero = int(input())
        numeros.append(numero)

    if len(numeros) != 100:
        print('Digite exatamente 100 números inteiros.')
        return

    soma = sum(numeros)
    media = soma / len(numeros)
    return media

def main():
    print("Digite 100 números inteiros: ")
    media = calcular_media()
    print(f"A média desses números é: {media:.2f}")

if __name__ == "__main__":
    main()
