def multiplica_constante(lista, constante):
    return [x * constante for x in lista]

def ler_numeros():
    numeros = []
    while True:
        numero = int(input("Digite um número inteiro (0 para encerrar): "))
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def ler_constante():
    return int(input("Digite um valor inteiro constante: "))

def exibir_nova_lista(nova_lista):
    print("Nova lista com os elementos multiplicados pela constante:")
    print(nova_lista)

def main():
    numeros = ler_numeros()
    constante = ler_constante()
    nova_lista = multiplica_constante(numeros, constante)
    exibir_nova_lista(nova_lista)

if __name__ == "__main__":
    main()
