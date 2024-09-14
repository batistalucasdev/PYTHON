def cifra_cesar(texto, chave, modo='criptografar'):
    resultado = ""
    if modo == 'descriptografar':
        chave = -chave
    
    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            nova_letra = chr((ord(caractere) - base + chave) % 26 + base)
            resultado += nova_letra
        else:
            resultado += caractere
    return resultado

modo = input("Você deseja criptografar ou descriptografar? (Digite 'criptografar' ou 'descriptografar'): ").strip().lower()

mensagem = input("Digite a mensagem: ")

chave = int(input("Digite a chave de criptografia (um número inteiro): "))

resultado = cifra_cesar(mensagem, chave, modo)

print(f"Resultado: {resultado}")
