def info(nome,estado_civil):
    contar_caracteres=len(nome)
    if estado_civil==1:
        conjuge=input().strip()
        contar_caracteres+=len(conjuge)
    return contar_caracteres

def main():
    nome=input().strip()
    estado_civil=int(input())
    caracteres=info(nome,estado_civil)
    print(f'{caracteres}')
                
if __name__ == '__main__':
    main()
