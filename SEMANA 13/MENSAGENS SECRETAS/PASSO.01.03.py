mensagem = input("Digite a mensagem para criptografar: ")

chave = int(input("Digite a chave de criptografia (um número inteiro): "))

mensagem_criptografada = ""

for caractere in mensagem:
    if caractere.isalpha():
        base = ord('A') if caractere.isupper() else ord('a')
        nova_letra = chr((ord(caractere) - base + chave) % 26 + base)
        mensagem_criptografada += nova_letra
    else:
        mensagem_criptografada += caractere

print("Mensagem criptografada:", mensagem_criptografada)
