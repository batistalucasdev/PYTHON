#lista de letras para criptografar
alfabeto = "abcdefghijklmnopqrstuvwxyz"

#a chave secreta é 3
#-3 para descriptografar
chave = -3

letra = input("Por favor, entre com uma letra para descriptografar: ")

#encontra a posição da letra em alfabeto
#exemplo: 'a' está na posição 0, 'e' está na posição 4, etc.
posicao = alfabeto.find(letra)

#some a chave secreta para encontrar a posição da letra criptografada
#% 26 significa 'volte para 0 quanado você chegar no 26'
novaPosicao = (posicao + chave) % 26

#a letra criptografada está no alfabeto na nova posição
letraCriptografada = alfabeto[novaPosicao]

print("Sua letra descriptografada é", letraCriptografada)
