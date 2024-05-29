def max_min(num1,num2,num3,num4,num5):
    maior = num1
    menor = num1

    if num2 > maior:
        maior = num2
    elif num2 < menor:
        menor = num2

    if num3 > maior:
        maior = num3
    elif num3 < menor:
        menor = num3

    if num4 > maior:
        maior = num4
    elif num4 < menor:
        menor = num4
        
    if num5 > maior:
        maior = num5
    elif num5 < menor:
        menor = num5

    return f'{maior}\n{menor}'

def main ():
    num1=int(input())
    num2=int(input())
    num3=int(input())
    num4=int(input())
    num5=int(input())
    
    numero=max_min(num1,num2,num3,num4,num5)
    print(numero)

if __name__ == '__main__':
    main()
