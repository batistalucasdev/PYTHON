from random import choice

executa = True

adjetivos = ["maravilhoso", "acima da média", "excelente"]
hobbies = ["andar de bicicleta", "programar", "fazer chá"]

print("Gerador de Cumprimentos")
print("--------------------")

nome = input("Qual é o seu nome?: ")

print('''
Menu
    c = obter cumprimento
    a = adicionar hobby
    d = remover hobby
    p = imprimir hobbies
    q = sair
''')

while executa:
    menuChoice = input("\n>_").lower()

    # 'c' para cumprimento
    if menuChoice == 'c':
        print("\nAqui está o seu cumprimento,", nome, ".")
        print(nome, "você é", choice(adjetivos), "em", choice(hobbies))
        print("De nada!")

    # 'a' para adicionar hobby
    elif menuChoice == 'a':
        itemToAdd = input("Adicione o hobby: ")
        if itemToAdd not in hobbies:
            hobbies.append(itemToAdd)
            print("Hobby adicionado com sucesso!")
        else:
            print("Esse hobby já está na lista!")

    # 'd' para remover um hobby
    elif menuChoice == 'd':
        itemToDelete = input("Insira o hobby a ser removido: ")
        if itemToDelete in hobbies:
            hobbies.remove(itemToDelete)
            print("Hobby removido com sucesso!")
        else:
            print("O hobby não está na lista!")

    # 'p' para imprimir a lista de hobbies
    elif menuChoice == 'p':
        print("Hobbies atuais:", hobbies)
  
    # 'q' para sair
    elif menuChoice == 'q':
        executa = False

    else:
        print("Escolha uma opção válida!")
