def calcular_media(numeros):
    if numeros:
        return sum(numeros) / len(numeros)
    return None

def main():
    numeros = []
    
    while True:
        numero = int(input("Digite um número inteiro positivo (ou 0 para terminar): "))
        if numero == 0:
            break
        if numero > 0:
            numeros.append(numero)
        else:
            print("Por favor, digite um número inteiro positivo.")
    
    media = calcular_media(numeros)
    if media is not None:
        print(f"A média aritmética dos números digitados é: {media:.2f}")
    else:
        print("Nenhum número válido foi inserido.")

if __name__ == "__main__":
    main()
