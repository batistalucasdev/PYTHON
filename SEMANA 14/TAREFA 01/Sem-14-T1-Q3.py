def gerar_lista():
    lista = []
    print("Digite 20 números inteiros:")
    for i in range(20):
        numero = int(input(f"Número {i+1}: "))
        lista.append(numero)
    return lista

def soma_listas(lista1, lista2):
    lista_soma = []
    for i in range(len(lista1)):
        lista_soma.append(lista1[i] + lista2[i])
    return lista_soma

def exibir_lista(lista, nome):
    print(f"\nLista {nome}: {lista}")

def main():
    A = gerar_lista()
    B = gerar_lista()

    C = soma_listas(A, B)

    exibir_lista(A, 'A')
    exibir_lista(B, 'B')
    exibir_lista(C, 'C')

if __name__ == "__main__":
    main()
