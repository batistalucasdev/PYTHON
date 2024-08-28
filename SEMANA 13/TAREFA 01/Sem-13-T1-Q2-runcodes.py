def criar_lista_com_zeros(n):
    lista = [0] * n
    return lista

def preencher_lista_com_sequencia(n):
    lista = [i + 1 for i in range(n)]
    return lista

def preencher_lista_com_entradas(n):
    lista = []
    for i in range(n):
        valor = int(input())
        lista.append(valor)
    return lista

def preencher_lista_com_entradas_invertidas(n):
    lista = []
    for i in range(n):
        valor = int(input())
        lista.insert(0, valor)
    return lista

def main():
    n = int(input())

    lista_zeros = criar_lista_com_zeros(n)
    print(lista_zeros)

    lista_sequencia = preencher_lista_com_sequencia(n)
    print(lista_sequencia)

    lista_entrada = preencher_lista_com_entradas(n)
    print(lista_entrada)

    lista_invertida = preencher_lista_com_entradas_invertidas(n)
    print(lista_invertida)

if __name__ == "__main__":
    main()