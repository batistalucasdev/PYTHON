def inverter_numero(numero):
    numero_invertido = 0
    while numero > 0:
        ultimo_digito = numero % 10
        numero_invertido = numero_invertido * 10 + ultimo_digito
        numero = numero // 10
    return numero_invertido

def main():
    numero = int(input())
    
    numero_invertido = inverter_numero(numero)
    
    print(f"{numero_invertido}")

if __name__ == "__main__":
    main()
