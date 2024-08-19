def saudacao():
    print("1 - Olá. Como vai?")

def bronca():
    print("2 - Vamos estudar mais.")

def felicitacao():
    print("3 - Meus Parabéns!")

def fim():
    print("0 - Fim de serviço.")

def opcao_invalida():
    print("Opção inválida.")

def mostrar_menu():
    print("OPÇÕES:")
    print("1 - SAUDAÇÃO")
    print("2 - BRONCA")
    print("3 - FELICITAÇÃO")
    print("0 - FIM")

def main():
    while True:
        mostrar_menu()
        opcao = input().strip()
        
        if opcao == "1":
            saudacao()
        elif opcao == "2":
            bronca()
        elif opcao == "3":
            felicitacao()
        elif opcao == "0":
            fim()
            break
        else:
            opcao_invalida()

if __name__ == "__main__":
    main()
