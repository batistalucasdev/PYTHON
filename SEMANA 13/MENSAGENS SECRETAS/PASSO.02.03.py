def calcular_compatibilidade(nome1, nome2):
    letras_amor = "amor"
    vogais = "aeiou"
    
    placar = 0
    
    for letra in nome1.lower() + nome2.lower():
        if letra in letras_amor:
            placar += 10
        if letra in vogais:
            placar += 5
    
    return placar

def avaliar_compatibilidade():
    print("Calculadora do Amor")
    print("＜3く3く3＜3く3＜3＜3")
    
    nome1 = input("Digite o nome da primeira pessoa: ")
    nome2 = input("Digite o nome da segunda pessoa: ")
    
    placar = calcular_compatibilidade(nome1, nome2)
    
    print(f"Seu placar de compatibilidade: {placar}")
    
    if placar > 80:
        print("Vocês terão um relacionamento muito intenso! <3")
    elif placar > 50:
        print("Vocês são compatíveis, mas há espaço para crescer! :)")
    else:
        print("Pode ser um desafio, mas tudo é possível! :-|")

avaliar_compatibilidade()
