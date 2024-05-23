def info(nome,estado_civil):
    contar_caracteres=len(nome)
    if estado_civil==1:
        conjuge=input('Digite o nome do cônjuge: ').strip()
        contar_caracteres+=len(conjuge)
    return contar_caracteres

def main():
    nome=input('Digite seu nome: ').strip()
    estado_civil=int(input('Informe seu estado civil (1 para casado ou 2 para solteiro):'))
    caracteres=info(nome,estado_civil)
    print(f'O total de caracteres é: {caracteres}')
                
if __name__ == '__main__':
    main()
