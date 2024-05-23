def contar_digitos_pares(numero):
    contar_digitos=0
    milhar=numero//1000
    centena=numero//100
    dezena=(numero//10)%10
    unidade=numero%10

    if numero < 100:
        if dezena%2==0:
            contar_digitos+=1
        
        if unidade%2==0:
            contar_digitos+=1

        return contar_digitos

    if 100 <= numero <= 999:
        if centena%2==0:
            contar_digitos+=1

        if dezena%2==0:
            contar_digitos+=1
        
        if unidade%2==0:
            contar_digitos+=1

        return contar_digitos

    if numero > 999:
        if milhar%2==0:
            contar_digitos+=1
            
        if centena%2==0:
            contar_digitos+=1

        if dezena%2==0:
            contar_digitos+=1
        
        if unidade%2==0:
            contar_digitos+=1

        return contar_digitos
    
def main():
    numero=int(input())
    total_digitos_pares=contar_digitos_pares(numero)
    print(f'{total_digitos_pares}')
        
if __name__ == '__main__':
    main()
