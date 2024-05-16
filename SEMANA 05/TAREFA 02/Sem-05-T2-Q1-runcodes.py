def vogal(char):
    vogais = 'aeiouAEIOU'
    return char in vogais

def main():
    caractere=input()
    print(f'{vogal(caractere)}')

if __name__ == '__main__':
    main()
