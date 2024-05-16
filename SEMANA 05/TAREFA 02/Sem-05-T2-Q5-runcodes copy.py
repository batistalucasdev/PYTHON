def mensagem(caractere):
    if caractere.isalpha():
        vogais = 'aeiouAEIOU'
        if caractere in vogais:
            return 'vogal'
        else:
            return 'consoante'
    elif caractere.isdigit():
        return 'número'
    else:
        return 'símbolo'

def main():
    caractere = input("Digite um caractere: ")
    print(mensagem(caractere))

if __name__ == '__main__':
    main()
