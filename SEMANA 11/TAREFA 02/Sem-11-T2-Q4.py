def calcular_total():
    precos = {
        'H': 5.50,
        'C': 6.80,
        'M': 4.50,
        'A': 7.00,
        'Q': 4.00
    }
    total = 0.0
    
    while True:
        print("CÓDIGO  PRODUTO         PREÇO (R$)\n"
              "H       Hamburger       5,50\n"
              "C       Cheeseburger    6,80\n"
              "M       Misto Quente    4,50\n"
              "A       Americano       7,00\n"
              "Q       Queijo Prato    4,00\n"
              "X       PARA TOTAL DA CONTA")
        
        codigo = input().strip().upper()
        if codigo == 'X':
            break
        
        if codigo in precos:
            total += precos[codigo]
    
    print(f"{total:.2f}")

if __name__ == "__main__":
    calcular_total()
