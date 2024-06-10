def numeros():
    sequencia = ""
    for i in range(10, 1010, 10):
        sequencia += str(i)
        if i < 1000:
            sequencia += ', '
    sequencia += '.'

    return sequencia

def main():
    resultado=numeros()
    print(resultado)

if __name__ == '__main__':
    main()
