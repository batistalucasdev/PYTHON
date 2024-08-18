def ler_numeros():
    numeros = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def calcular_soma(numeros):
    return sum(numeros)

def main():
    numeros = ler_numeros()
    soma = calcular_soma(numeros)
    print(f"{soma}")

if __name__ == "__main__":
    main()
