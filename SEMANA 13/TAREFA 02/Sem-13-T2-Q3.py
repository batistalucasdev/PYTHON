def ler_notas(num_alunos):
    notas = []
    for i in range(num_alunos):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)
    return notas

def alunos_aprovados(notas, nota_minima=6):
    indices_aprovados = []
    for i, nota in enumerate(notas):
        if nota >= nota_minima:
            indices_aprovados.append(i)
    return indices_aprovados

def main():
    num_alunos = 50
    notas = ler_notas(num_alunos)
    indices_aprovados = alunos_aprovados(notas)
    print("Índices dos alunos com nota maior ou igual a 6:", indices_aprovados)

if __name__ == "__main__":
    main()
