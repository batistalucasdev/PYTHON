def verificar_numero(numero):
    dezena=numero//10
    unidade=numero%10
        
    if dezena%2==0 and unidade%2==0:
        print('Nenhum dígito é ímpar.')
        
    elif dezena%2!=0 and unidade%2!=0:
        print('Os dois dígitos são ímpares.')
        
    else:
        print('Apenas um dígito é ímpar.')

def main():
    numero=int(input('Digite um número entre 10 e 99: '))

    if 10 <= numero <= 99:
        verificar_numero(numero)
        
if __name__ == '__main__':
    main()
