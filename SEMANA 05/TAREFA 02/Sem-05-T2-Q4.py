def eh_letra(caractere):
    return (caractere >= 'a' and caractere <= 'z') or (caractere >= 'A' and caractere <= 'Z')

def numero(caractere):
    return (caractere>='1' and caractere<='9')

def main():
    caractere = input('Digite um caractere: ')
    print(eh_letra(caractere) or numero(caractere))

if __name__ == '__main__':
    main()
