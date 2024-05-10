altura=int(input('Digite o valor da altura: '))
comprimento=int(input('Digite o valor do comprimento: '))
largura=int(input('Digite o valor da largura: '))
a_piso=largura*comprimento
v_sala=largura*comprimento*altura
a_parede=2*altura*largura+2*altura*comprimento
print(f'A área do piso é: {a_piso} m²')
print(f'O volume da sala é: {v_sala} m³')
print(f'A área da parede é: {a_parede} m²')
