def fatorial(n):
    if n == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        return resultado

def main():
    entrada = input("Digite um número inteiro não-negativo: ")
    
    if entrada.isdigit():
        numero = int(entrada)
        if numero >= 0:
            print(f"O fatorial de {numero} é {fatorial(numero)}")
        else:
            print("Por favor, insira um número inteiro não-negativo.")
    else:
        print("Entrada inválida! Por favor, insira um número inteiro não-negativo.")

if __name__ == "__main__":
    main()
