def ler_numeros(qtd):
    numeros = []
    for i in range(qtd):
        numero = float(input())
        numeros.append(numero)
    return numeros

def contar_negativos(numeros):
    return sum(1 for num in numeros if num < 0)

def soma_positivos(numeros):
    return int(sum(num for num in numeros if num > 0))

def main():
    qtd = 10
    numeros = ler_numeros(qtd)
    negativos = contar_negativos(numeros)
    positivos_soma = soma_positivos(numeros)
    
    numeros_inteiros = [int(num) for num in numeros]
    
    print(numeros_inteiros)
    print(negativos)
    print(positivos_soma)

if __name__ == "__main__":
    main()
