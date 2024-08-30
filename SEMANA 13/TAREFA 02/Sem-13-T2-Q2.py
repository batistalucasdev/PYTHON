def ler_numeros(qtd):
    numeros = []
    for _ in range(qtd):
        numero = int(input(f"Digite o número {_+1}/{qtd}: "))
        numeros.append(numero)
    return numeros

def ordenar_numeros(numeros):
    return sorted(numeros)

def multiplicar_indices(numeros):
    resultado = []
    for i, numero in enumerate(numeros):
        if i % 2 == 0:
            resultado.append(numero * 3)
        else:
            resultado.append(numero * 5)
    return resultado

def main():
    qtd = 100
    numeros = ler_numeros(qtd)
    numeros_ordenados = ordenar_numeros(numeros)
    numeros_multiplicados = multiplicar_indices(numeros_ordenados)
    
    print("\nNúmeros lidos ordenados:")
    print(numeros_ordenados)
    
    print("\nNúmeros multiplicados:")
    print(numeros_multiplicados)

if __name__ == "__main__":
    main()
