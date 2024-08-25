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

def print_primes(x, y):
    if x > y:
        x, y = y, x
    for num in range(x, y + 1):
        if is_prime(num):
            print(num)

def main():
    x = int(input())
    y = int(input())
    print_primes(x, y)

if __name__ == "__main__":
    main()
