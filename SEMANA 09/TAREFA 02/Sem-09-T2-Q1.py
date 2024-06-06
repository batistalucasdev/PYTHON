def semana(num):

    if num == 1:
        return 'domingo'
    if num == 2:
        return 'segunda-feira'
    if num == 3:
        return 'terça-feira'
    if num == 4:
        return 'quarta-feira'
    if num == 5:
        return 'quinta-feira'
    if num == 6:
        return 'sexta-feira'
    if num == 7:
        return 'sábado'
    else:
        return 'valor inválido'
       
def main():
    num=int(input("Digite um número (1-domingo, 2-segunda-feira, 3-terça-feira, 4-quarta-feira, 5-quinta-feira, 6-sexta-feira, sábado): "))
    
    resultado=semana(num)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
