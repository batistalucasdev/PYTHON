def calcular_media_final(nota1,nota2,nota3,media_exercicios):
    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios)/7

    if media_final >= 9.0:
        return 'A'
        if 'A':
            return f'A \nAprovado'
    elif 7.5 <= media_final < 9.0:
        return f'B \nAprovado'
        if 'B':
            return 'Aprovado'
    elif 6.0 <= media_final < 7.5:
        return 'C'
        if 'C':
            return f'C \nAprovado'
    elif 4.0 <= media_final < 6.0:
        return 'D'
        if 'D':
            return f'D \nReprovado'
    elif media_final < 4.0:
        return 'E'
        if 'E':
            return f'E \nReprovado'
    else:
        raise ValueError(f'Informação inválida: {media_final}')

def main():
    matricula=input("Digite o número de matrícula do aluno: ")
    nota1=float(input("Digite a primeira nota: "))
    nota2=float(input("Digite a segunda nota: "))
    nota3=float(input("Digite a terceira nota: "))
    media_exercicios=float(input("Digite a média das notas obtidas nos exercícios que fazem parte da sua avaliação: "))

    media_final = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios)/7
    
    resultado=calcular_media_final(nota1,nota2,nota3,media_exercicios)
    print(f'A matrícula do aluno é: {matricula}')
    print(f'{media_final:.2f}')
    print(f'{resultado}')

if __name__ == '__main__':
    main()
