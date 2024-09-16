def jogador_mais_alto(jogadores):
    mais_alto = jogadores[0]
    for jogador in jogadores:
        if jogador[1] > mais_alto[1]:
            mais_alto = jogador
    return mais_alto

def media_altura(jogadores):
    soma_alturas = 0
    for jogador in jogadores:
        soma_alturas += jogador[1]
    return soma_alturas / len(jogadores)

def jogadores_acima_media(jogadores, media):
    acima_media = []
    for jogador in jogadores:
        if jogador[1] > media:
            acima_media.append(jogador)
    return acima_media

def main():
    jogadores = []
    for i in range(12):
        nome = input(f"Digite o nome do jogador {i+1}: ")
        altura = float(input(f"Digite a altura (em metros) do jogador {i+1}: "))
        jogadores.append((nome, altura))

    mais_alto = jogador_mais_alto(jogadores)
    print("JOGADOR MAIS ALTO DO TIME")
    print(f"{mais_alto[0]} com {mais_alto[1]:.2f} metros.")

    media = media_altura(jogadores)
    print("ALTURA MÉDIA DO TIME")
    print(f"{media:.2f} metros.")

    acima_media = jogadores_acima_media(jogadores, media)
    print("JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME")
    for jogador in acima_media:
        print(f"{jogador[0]}\n{jogador[1]:.2f} metros")

if __name__ == "__main__":
    main()
