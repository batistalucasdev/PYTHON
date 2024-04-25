def calcular_media(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

def main():
    entrada = input("Digite 100 números inteiros: ")
    numeros = [int(numero) for numero in entrada.split()]

    if len(numeros) != 4:
        print("Você deve inserir exatamente 4 números inteiros.")
        return

    media = calcular_media(numeros)
    print(f"A média desses números é: {media}")

if __name__ == "__main__":
    main()
