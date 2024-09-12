def leitura_numeros():
    numeros = []
    for i in range(10):
        numero = int(input(f"Digite um número: "))
        numeros.append(numero)
    return numeros

def calcular_soma(numeros):
    return sum(numeros)

def calcular_multiplicacao(numeros):
    multiplicacao = 1
    for i in numeros:
        multiplicacao = multiplicacao * i
    return multiplicacao

def main():
    numeros = leitura_numeros()
    soma = calcular_soma(numeros)
    multiplicacao = calcular_multiplicacao(numeros)

    print(f"Números: {numeros}")
    print(f"Soma dos números: {soma}")
    print(f"Multiplicação dos números: {multiplicacao}")
    
if __name__ == "__main__":
    main()
