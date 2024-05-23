def main():
    num1=int(input('Digite o primeiro número: '))
    num2=int(input('Digite o segundo número: '))
    num3=int(input('Digite o terceiro número: '))
    
    if num1 >= num2 and num1 >= num3:
        maior = num1
        if num2 >= num3:
            medio = num2
            menor = num3
        else:
            medio = num3
            menor = num2
            
    elif num2 >= num1 and num2 >= num3:
        maior = num2
        if num1 >= num3:
            medio = num1
            menor = num3
        else:
            medio = num3
            menor = num1
            
    else:
        maior = num3
        if num1 >= num2:
            medio = num1
            menor = num2
        else:
            medio = num2
            menor = num1
            
    print(f'O número menor é {menor}')
    print(f'O número médio é {medio}')
    print(f'O número maior é {maior}')

if __name__ == '__main__':
    main()
