from random import choice

def main():
    executa = True
    nomes_machos = ["Rex", "Max", "Thor"]
    nomes_femeas = ["Luna", "Bella", "Maya"]
    nomes_gerais = ["Pipoca", "Bolota", "Tigrão"]

    print("Gerador de Nomes para Animais de Estimação")
    print("------------------------------------------")

    print('''
Menu
    m = obter nome para macho
    f = obter nome para fêmea
    t = obter nome para tipo de animal específico
    a = adicionar nome
    d = remover nome
    p = imprimir lista de nomes
    q = sair
''')

    while executa:
        menuChoice = input("\n>_").lower()

        # 'm' para obter nome para macho
        if menuChoice == 'm':
            qtd_nomes = int(input("Quantos nomes você precisa para animais machos? "))
            for _ in range(qtd_nomes):
                print("Nome sugerido para macho:", choice(nomes_machos))

        # 'f' para obter nome para fêmea
        elif menuChoice == 'f':
            qtd_nomes = int(input("Quantos nomes você precisa para animais fêmeas? "))
            for _ in range(qtd_nomes):
                print("Nome sugerido para fêmea:", choice(nomes_femeas))

        # 't' para obter nome de tipo específico de animal
        elif menuChoice == 't':
            tipo_animal = input("Qual é o tipo do animal (ex: cachorro, gato, pássaro)?: ").lower()
            if tipo_animal == "cachorro":
                print("Nome sugerido para cachorro:", choice(nomes_gerais))
            elif tipo_animal == "gato":
                print("Nome sugerido para gato:", choice(nomes_gerais))
            else:
                print(f"Nome sugerido para {tipo_animal}:", choice(nomes_gerais))

        # 'a' para adicionar nome
        elif menuChoice == 'a':
            genero = input("O nome é para macho (m) ou fêmea (f) ou geral (g)?: ").lower()
            nome = input("Adicione o nome: ")
            if genero == 'm' and nome not in nomes_machos:
                nomes_machos.append(nome)
                print("Nome para macho adicionado com sucesso!")
            elif genero == 'f' and nome not in nomes_femeas:
                nomes_femeas.append(nome)
                print("Nome para fêmea adicionado com sucesso!")
            elif genero == 'g' and nome not in nomes_gerais:
                nomes_gerais.append(nome)
                print("Nome geral adicionado com sucesso!")
            else:
                print("Esse nome já está na lista!")

        # 'd' para remover nome
        elif menuChoice == 'd':
            genero = input("O nome é para macho (m), fêmea (f) ou geral (g)?: ").lower()
            nome = input("Insira o nome a ser removido: ")
            if genero == 'm' and nome in nomes_machos:
                nomes_machos.remove(nome)
                print("Nome de macho removido com sucesso!")
            elif genero == 'f' and nome in nomes_femeas:
                nomes_femeas.remove(nome)
                print("Nome de fêmea removido com sucesso!")
            elif genero == 'g' and nome in nomes_gerais:
                nomes_gerais.remove(nome)
                print("Nome geral removido com sucesso!")
            else:
                print("O nome não está na lista!")

        # 'p' para imprimir a lista de nomes
        elif menuChoice == 'p':
            print("Nomes para machos:", nomes_machos)
            print("Nomes para fêmeas:", nomes_femeas)
            print("Nomes gerais:", nomes_gerais)

        # 'q' para sair
        elif menuChoice == 'q':
            executa = False

        else:
            print("Escolha uma opção válida!")


if __name__ == "__main__":
    main()
