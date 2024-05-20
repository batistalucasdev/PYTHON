def temperatura(celsius):
    return (celsius*(9/5))+32

def main():
    celsius=float(input())
    fahrenheit=temperatura(celsius)
    print(f'{fahrenheit:.2f}')

if __name__ == '__main__':
    main()
