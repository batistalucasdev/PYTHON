def obter_preco(codigo):
    """Retorna o preço do item com base no código."""
    precos = {
        'H': 5.50,
        'C': 6.80,
        'M': 4.50,
        'A': 7.00,
        'Q': 4.00
    }
    return precos.get(codigo.upper(), 0)

def calcular_total():
    """Calcula o total a pagar com base nos itens comprados."""
    total = 0.0
    
    while True:
        codigo = input().strip().upper()
        if codigo == 'X':
            break
        
        preco = obter_preco(codigo)
        if preco == 0:
            continue
        
        total += preco
    
    return total

def exibir_cardapio():
    """Exibe o cardápio com os preços dos produtos."""
    print("CÓDIGO  PRODUTO         PREÇO (R$)")
    print("H       Hamburger       5,50")
    print("C       Cheeseburger    6,80")
    print("M       Misto Quente    4,50")
    print("A       Americano       7,00")
    print("Q       Queijo Prato    4,00")
    print("X       PARA TOTAL DA CONTA")

def main():
    """Função principal para executar o programa."""
    exibir_cardapio()  # Exibe o cardápio
    total_a_pagar = calcular_total()
    print(f"{total_a_pagar:.2f}")

if __name__ == "__main__":
    main()
