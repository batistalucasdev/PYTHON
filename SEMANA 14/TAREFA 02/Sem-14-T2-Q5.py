def unir_listas(lista1, lista2):
    lista_unida = []
    for item in lista1 + lista2:
        if item not in lista_unida:
            lista_unida.append(item)
    return lista_unida

def main():
    lista1 = []
    lista2 = []
    print("Digite os elementos da primeira lista:")
    for i in range(10):
        lista1.append(int(input((f"Elemento {i+1}: "))))
    print("Digite os elementos da segunda lista:")
    for i in range(10):
        lista2.append(int(input((f"Elemento {i+1}: "))))
    
    lista_unida = unir_listas(lista1, lista2)
    print("União das duas listas:",lista_unida)

if __name__ == "__main__":
    main()
