import random

def embaralhar_alfabeto():
    alfabeto = list('abcdefghijklmnopqrstuvwxyz')
    random.shuffle(alfabeto)
    return ''.join(alfabeto)

def cifra_cesar_customizada(texto, chave_inicial, alfabeto_embaralhado, modo='criptografar'):
    resultado = ""
    chave = chave_inicial

    for caractere in texto:
        if caractere.isalpha():
            base = ord('A') if caractere.isupper() else ord('a')
            indice_original = ord(caractere.lower()) - ord('a')
            if modo == 'criptografar':
                indice_criptografado = (indice_original + chave) % 26
            else:
                indice_criptografado = (indice_original - chave) % 26

            nova_letra = alfabeto_embaralhado[indice_criptografado]
            nova_letra = nova_letra.upper() if caractere.isupper() else nova_letra
            resultado += nova_letra

            chave += 1
        elif modo == 'criptografar':
            continue
        else:
            resultado += caractere

    return resultado

alfabeto_embaralhado = embaralhar_alfabeto()
print(f"Alfabeto embaralhado: {alfabeto_embaralhado}")

modo = input("Você deseja criptografar ou descriptografar? (Digite 'criptografar' ou 'descriptografar'): ").strip().lower()

mensagem = input("Digite a mensagem: ")

chave_inicial = int(input("Digite a chave inicial de criptografia (um número inteiro): "))

resultado = cifra_cesar_customizada(mensagem, chave_inicial, alfabeto_embaralhado, modo)

print(f"Resultado: {resultado}")
