def vogal(caractere):
    vogais = 'aeiouAEIOU'
    return caractere in vogais

def letra(caractere):
    return 'A' <= caractere.upper() <= 'Z'
    
def consoante(caractere):
    return letra(caractere) and not vogal(caractere)

def numero(caractere):
    return '0' <= caractere <= '9'

def simbolo(caractere):
    return not letra(caractere) and not numero(caractere)

def main():
    caractere=input()
    if vogal(caractere):
        print('vogal')
    elif consoante(caractere):
        print('consoante')
    elif numero(caractere):
        print('número')
    else:
        print('símbolo')

if __name__ == '__main__':
    main()
