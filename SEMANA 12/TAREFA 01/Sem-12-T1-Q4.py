def numero_da_sorte(data_nascimento):
    return sum(int(digito) for digito in data_nascimento)

def main():
    data_nascimento = input("Digite sua data de nascimento no formato ddmmaaaa: ")
    sorte = numero_da_sorte(data_nascimento)
    print(f"Seu número da sorte é: {sorte}")

if __name__ == "__main__":
    main()
