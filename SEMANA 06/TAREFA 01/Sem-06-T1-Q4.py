def maximo(num1,num2,num3,num4,num5):
    return max(num1,num2,num3,num4,num5)

def minimo(num1,num2,num3,num4,num5):
    return min(num1,num2,num3,num4,num5)

def calculo_media(num1,num2,num3,num4,num5):
    return (num1+num2+num3+num4+num5)/5

def main():
    num1=int(input('Digite o primeiro número: '))
    num2=int(input('Digite o segundo número: '))
    num3=int(input('Digite o terceiro número: '))
    num4=int(input('Digite o quarto número: '))
    num5=int(input('Digite o quinto número: '))
    maior=maximo(num1,num2,num3,num4,num5)
    menor=minimo(num1,num2,num3,num4,num5)
    media=calculo_media(num1,num2,num3,num4,num5)
    print(f'O maior número lido é: {maior}')
    print(f'O menor número lido é: {menor}')
    print(f'A média aritmética dos números lidos é: {media}')


if __name__ == '__main__':
    main()
