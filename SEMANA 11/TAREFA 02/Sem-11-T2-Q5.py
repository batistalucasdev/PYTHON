def ler_nota():
    while True:
        try:
            nota = float(input("Digite a nota do aluno (entre 0 e 10): "))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

def calcular_conceito(nota):
    if nota >= 8.5:
        return "A"
    elif nota >= 7.0:
        return "B"
    elif nota >= 5.0:
        return "C"
    elif nota >= 4.0:
        return "D"
    else:
        return "E"

def main():
    nota = ler_nota()
    conceito = calcular_conceito(nota)
    print(f"A nota do aluno é {nota:.1f}, o conceito correspondente é {conceito}.")

if __name__ == "__main__":
    main()
