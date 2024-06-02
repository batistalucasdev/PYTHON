def ler_numero(num1,num2,num3):

    if num1 == num2 and num2 == num3 and num1 == num3:
        return 'Todos os valores são iguais'
    if num1 == num2 or num1 == num3 or num2 == num3:
        return 'Existem dois valores iguais e um diferente'
    if num1 != num2 or num1 != num3 or num2 != num3:
        return 'Todos os valores são diferentes'    
    else:
        raise ValueError(f'Informação inválida')

def main():
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    num3=int(input("Digite o terceiro número: "))
    
    print(ler_numero(num1,num2,num3))

if __name__ == '__main__':
    main()
