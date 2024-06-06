def extenso(numero):
    centena = numero // 100
    dezena = (numero % 100) // 10
    unidade = numero % 10
    texto = ""

    if centena > 0:
        if centena == 1:
            texto = "uma centena"
        elif centena == 2:
            texto = "duas centenas"
        elif centena == 3:
            texto = "três centenas"
        elif centena == 4:
            texto = "quatro centenas"
        elif centena == 5:
            texto = "cinco centenas"
        elif centena == 6:
            texto = "seis centenas"
        elif centena == 7:
            texto = "sete centenas"
        elif centena == 8:
            texto = "oito centenas"
        elif centena == 9:
            texto = "nove centenas"

    if dezena > 0:
        if centena > 0 and unidade != 0:
            texto += ", "
        if centena > 0 and unidade == 0:
            texto += " e "
        if dezena == 1:
            texto += "uma dezena"
        elif dezena == 2:
            texto += "duas dezenas"
        elif dezena == 3:
            texto += "três dezenas"
        elif dezena == 4:
            texto += "quatro dezenas"
        elif dezena == 5:
            texto += "cinco dezenas"
        elif dezena == 6:
            texto += "seis dezenas"
        elif dezena == 7:
            texto += "sete dezenas"
        elif dezena == 8:
            texto += "oito dezenas"
        elif dezena == 9:
            texto += "nove dezenas"

    if unidade > 0:
        if centena > 0 or dezena > 0:
            texto += " e "
        if unidade == 1:
            texto += "uma unidade"
        elif unidade == 2:
            texto += "duas unidades"
        elif unidade == 3:
            texto += "três unidades"
        elif unidade == 4:
            texto += "quatro unidades"
        elif unidade == 5:
            texto += "cinco unidades"
        elif unidade == 6:
            texto += "seis unidades"
        elif unidade == 7:
            texto += "sete unidades"
        elif unidade == 8:
            texto += "oito unidades"
        elif unidade == 9:
            texto += "nove unidades"

    return texto + "."

def main():
    numero = int(input("Digite um número inteiro menor que 1000: "))

    if numero < 1000:
        resultado = extenso(numero)
        print(f'Esse número por extenso é: {resultado}')
    else:
        print("Por favor, insira um número menor que 1000.")

if __name__ == '__main__':
    main()
