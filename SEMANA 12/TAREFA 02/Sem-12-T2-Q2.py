def fibonacci(n):
    fib_sequence = [0, 1]
    
    while len(fib_sequence) < n:
        next_term = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_term)
    
    return fib_sequence

def main():
    n = input("Digite o número de termos que você deseja na sequência de Fibonacci (maior ou igual a 2): ")
    
    if not n.isdigit():
        print("Por favor, insira um número inteiro válido.")
        return
    
    n = int(n)
    
    if n < 2:
        print("O valor deve ser maior ou igual a 2.")
        return
    
    fib_sequence = fibonacci(n)
    
    output = ""
    for i in range(n):
        if i > 0:
            output += ", "
        output += str(fib_sequence[i])
    
    print("Os primeiros", n, "termos da sequência de Fibonacci são:")
    print(output)

if __name__ == "__main__":
    main()
