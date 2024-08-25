def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def main():
    number_input = input()
    
    if number_input.isdigit() or (number_input[0] == '-' and number_input[1:].isdigit()):
        number = int(number_input)
        print(is_prime(number))
    else:
        print("Entrada inválida. Por favor, digite um número inteiro.")

if __name__ == "__main__":
    main()
