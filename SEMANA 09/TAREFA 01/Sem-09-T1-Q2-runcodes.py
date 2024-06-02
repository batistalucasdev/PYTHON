def executar_operacao(num1,num2,operacao):

    if operacao == 1:
        return num1 + num2
    if operacao == 2:
        return num1 - num2
    if operacao == 3:
        return num1 * num2
    if operacao == 4:
        return num1 / num2
    else:
        raise ValueError(f'Informação inválida')

def main():
    num1=int(input())
    num2=int(input())
    operacao=int(input())

    resultado=executar_operacao(num1,num2,operacao)
    print(f'{resultado:.2f}')

if __name__ == '__main__':
    main()
