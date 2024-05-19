def maximo(num1,num2,num3,num4,num5):
    return max(num1,num2,num3,num4,num5)

def minimo(num1,num2,num3,num4,num5):
    return min(num1,num2,num3,num4,num5)

def calculo_media(num1,num2,num3,num4,num5):
    return (num1+num2+num3+num4+num5)/5

def main():
    num1=int(input())
    num2=int(input())
    num3=int(input())
    num4=int(input())
    num5=int(input())
    maior=maximo(num1,num2,num3,num4,num5)
    menor=minimo(num1,num2,num3,num4,num5)
    media=calculo_media(num1,num2,num3,num4,num5)
    print(f'{maior}')
    print(f'{menor}')
    print(f'{media}')


if __name__ == '__main__':
    main()
