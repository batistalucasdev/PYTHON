def multiplica_constante(lista, constante):
    return [x * constante for x in lista]

def ler_numeros():
    numeros = []
    while True:
        numero = int(input())
        if numero == 0:
            break
        numeros.append(numero)
    return numeros

def ler_constante():
    return int(input())

def exibir_nova_lista(nova_lista):
    print(nova_lista)

def main():
    numeros = ler_numeros()
    constante = ler_constante()
    nova_lista = multiplica_constante(numeros, constante)
    exibir_nova_lista(nova_lista)

if __name__ == "__main__":
    main()
