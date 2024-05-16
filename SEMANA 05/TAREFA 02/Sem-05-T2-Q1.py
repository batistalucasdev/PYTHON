def vogal(char):
    vogais = 'aeiouAEIOU'
    return char in vogais

def main():
    caractere=input('Digite um caractere: ')
    print(f'{vogal(caractere)}')

if __name__ == '__main__':
    main()
