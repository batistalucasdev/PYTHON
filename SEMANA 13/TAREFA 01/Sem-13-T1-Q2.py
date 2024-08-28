def criar_lista_com_zeros(n):
    lista = [0] * n
    return lista

def preencher_lista_com_sequencia(n):
    lista = [i + 1 for i in range(n)]
    return lista

def preencher_lista_com_entradas(n):
    lista = []
    for i in range(n):
        valor = int(input(f"Digite o valor para a posição {i+1}: "))
        lista.append(valor)
    return lista

def preencher_lista_com_entradas_invertidas(n):
    lista = []
    for i in range(n):
        valor = int(input(f"Digite o valor para a posição {i+1}: "))
        lista.insert(0, valor)
    return lista

def main():
    n = int(input("Digite o número de posições da lista: "))

    lista_zeros = criar_lista_com_zeros(n)
    print("Lista preenchida com zeros:", lista_zeros)

    lista_sequencia = preencher_lista_com_sequencia(n)
    print("Lista preenchida com números de 1 a n:", lista_sequencia)

    lista_entrada = preencher_lista_com_entradas(n)
    print("Lista preenchida com valores lidos pelo teclado:", lista_entrada)

    lista_invertida = preencher_lista_com_entradas_invertidas(n)
    print("Lista preenchida na ordem inversa com valores lidos pelo teclado:", lista_invertida)

if __name__ == "__main__":
    main()
