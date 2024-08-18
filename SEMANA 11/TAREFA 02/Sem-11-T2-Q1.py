def ler_numeros():
    numeros = []
    while True:
        numero = int(input("Digite um número inteiro (0 para sair): "))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def calcular_soma(numeros):
    return sum(numeros)

def main():
    numeros = ler_numeros()
    soma = calcular_soma(numeros)
    print(f"A soma dos números digitados é: {soma}")

if __name__ == "__main__":
    main()
