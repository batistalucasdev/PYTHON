def numero_da_sorte(data_nascimento):
    return sum(int(digito) for digito in data_nascimento)

def main():
    data_nascimento = input()
    sorte = numero_da_sorte(data_nascimento)
    print(f"{sorte}")

if __name__ == "__main__":
    main()
