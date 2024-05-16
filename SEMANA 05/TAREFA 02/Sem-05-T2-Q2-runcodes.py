def eh_letra(caractere):
    return (caractere >= 'a' and caractere <= 'z') or (caractere >= 'A' and caractere <= 'Z')

def main():
    caractere = input()
    print(eh_letra(caractere))

if __name__ == '__main__':
    main()
