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
    num1=int(input("Digite o primeiro número: "))
    num2=int(input("Digite o segundo número: "))
    operacao=int(input("Digite qual operação a ser executada (1 – Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão): "))

    resultado=executar_operacao(num1,num2,operacao)
    print(f'O resultado da operação é: {resultado:.2f}')

if __name__ == '__main__':
    main()
