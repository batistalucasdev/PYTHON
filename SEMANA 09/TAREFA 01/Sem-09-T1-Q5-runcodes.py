def divisao(num):
    div = num % 5
    
    if div == 0:
        return 9 * num + 7
    if div == 1:
        if num % 2 == 0:
            return 'par'
        else:
            return 'ímpar'
    if div == 2:
        return 5 * num ** 2 - 3 * num + 42
    if div == 3:
        return num // 10
    if div == 4:
        return num ** 2
    else:
        raise ValueError(f'Informação inválida')
        
def main():
    num=int(input())
    
    resultado=divisao(num)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
