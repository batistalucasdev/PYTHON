def unir_listas(lista1, lista2):
    lista_unida = []
    for item in lista1 + lista2:
        if item not in lista_unida:
            lista_unida.append(item)
    return lista_unida

def main():
    lista1 = []
    lista2 = []
    for i in range(10):
        lista1.append(int(input()))
    for i in range(10):
        lista2.append(int(input()))
    
    lista_unida = unir_listas(lista1, lista2)
    print(lista_unida)

if __name__ == "__main__":
    main()
