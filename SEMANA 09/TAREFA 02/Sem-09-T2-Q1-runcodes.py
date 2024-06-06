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
    num=int(input())
    
    resultado=semana(num)
    print(f'{resultado}')

if __name__ == '__main__':
    main()
