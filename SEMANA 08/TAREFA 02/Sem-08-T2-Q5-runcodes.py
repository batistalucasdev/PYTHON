def calcular_media_final(nota1,nota2,nota3,media_exercicios):
    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios)/7

    if media_final >= 9.0:
        return f'A \nAprovado'
    elif 7.5 <= media_final < 9.0:
        return f'B \nAprovado'
    elif 6.0 <= media_final < 7.5:
        return f'C \nAprovado'
    elif 4.0 <= media_final < 6.0:
        return f'D \nReprovado'
    elif media_final < 4.0:
        return f'E \nReprovado'
    else:
        raise ValueError(f'Informação inválida: {media_final}')

def main():
    matricula=input()
    nota1=float(input())
    nota2=float(input())
    nota3=float(input())
    media_exercicios=float(input())

    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios)/7
    
    resultado=calcular_media_final(nota1,nota2,nota3,media_exercicios)
    print(f'{matricula}')
    print(f'{media_final:.2f}')
    print(f'{resultado}')

if __name__ == '__main__':
    main()
