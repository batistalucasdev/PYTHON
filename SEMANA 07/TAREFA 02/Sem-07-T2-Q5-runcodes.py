def main():
    num1=int(input())
    num2=int(input())
    num3=int(input())
    
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
            
    print(f'{menor}')
    print(f'{medio}')
    print(f'{maior}')

if __name__ == '__main__':
    main()
