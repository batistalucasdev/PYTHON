def eh_letra(caractere):
    return (caractere >= 'a' and caractere <= 'z') or (caractere >= 'A' and caractere <= 'Z')

def eh_consoante(caractere):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return eh_letra(caractere) and caractere not in vogais

def main():
    caractere = input()
    print(eh_consoante(caractere))

if __name__ == '__main__':
    main()
