def ler_idades():
    idades = []
    while True:
        idade = int(input())
        if idade == 0:
            break
        idades.append(idade)
    return idades

def calcular_numero_pessoas(idades):
    return len(idades)

def calcular_idade_media(idades):
    if len(idades) > 0:
        return sum(idades) / len(idades)
    return 0

def encontrar_menor_idade(idades):
    if len(idades) > 0:
        return min(idades)
    return None

def encontrar_maior_idade(idades):
    if len(idades) > 0:
        return max(idades)
    return None

def main():
    idades = ler_idades()
    
    numero_pessoas = calcular_numero_pessoas(idades)
    idade_media = calcular_idade_media(idades)
    menor_idade = encontrar_menor_idade(idades)
    maior_idade = encontrar_maior_idade(idades)
    
    print(f"{numero_pessoas}")
    print(f"{idade_media:.2f}")
    print(f"{menor_idade}")
    print(f"{maior_idade}")

if __name__ == "__main__":
    main()
