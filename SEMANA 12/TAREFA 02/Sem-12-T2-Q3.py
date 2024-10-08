def calcular_serie_harmonica(n):
    H = 0.0
    for i in range(1, n + 1):
        H += 1 / i
    return H

def main():
    n = input("Digite o valor de n: ")
    
    if n.isdigit():
        n = int(n)
        if n > 0:
            resultado = calcular_serie_harmonica(n)
            print(f"O valor de H com 4 casas decimais é: {resultado:.4f}")
        else:
            print("Erro: O valor de n deve ser um número inteiro positivo.")
    else:
        print("Erro: O valor de n deve ser um número inteiro.")

if __name__ == "__main__":
    main()
