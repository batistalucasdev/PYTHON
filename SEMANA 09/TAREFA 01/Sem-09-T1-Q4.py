def diferenca(num1,num2,num3):
    sub1 = abs(num1 - num2)
    sub2 = abs(num1 - num3)
    
    if sub1 > sub2:
        return sub2
    else:
        return sub1

def main():
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    num3=int(input("Digite o terceiro número: "))
    
    resultado=diferenca(num1,num2,num3)
    print(f'A diferença é: {resultado}')

if __name__ == '__main__':
    main()
