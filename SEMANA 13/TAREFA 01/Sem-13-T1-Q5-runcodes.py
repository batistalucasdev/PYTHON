def main():
    A = []
    B = []
    
    for i in range(25):
        while True:
            try:
                numero = int(input())
                A.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    for i in range(25):
        while True:
            try:
                numero = int(input())
                B.append(numero)
                break
            except ValueError:
                print("Por favor, digite um número inteiro válido.")

    C = []
    for a, b in zip(A, B):
        C.append(a)
        C.append(b)

    print(A)
    print(B)
    print(C)

if __name__ == "__main__":
    main()
