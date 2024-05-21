def media_notas(nota1,nota2,nota3):
    media=(nota1+nota2+nota3)/3
    if nota3 > 8:
        media=media+1
        if media > 10:
            media=10
    return media

def main():
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    nota3=float(input('Digite a terceira nota: '))
    resultado=media_notas(nota1,nota2,nota3)
    print(f'A média das notas é {resultado:.2f}')

if __name__ == '__main__':
    main()
