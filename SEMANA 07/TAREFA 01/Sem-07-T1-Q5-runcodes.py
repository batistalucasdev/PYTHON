def media_notas(nota1,nota2,nota3):
    media=(nota1+nota2+nota3)/3
    if nota3 > 8:
        media=media+1
        if media > 10:
            media=10
    return media

def main():
    nota1=float(input())
    nota2=float(input())
    nota3=float(input())
    resultado=media_notas(nota1,nota2,nota3)
    print(resultado)

if __name__ == '__main__':
    main()
