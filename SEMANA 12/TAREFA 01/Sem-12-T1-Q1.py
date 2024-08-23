def calcular_tempo_para_alcance(distancia_inicial, velocidade_tartaruga, velocidade_lebre):
    tempo = distancia_inicial / (velocidade_lebre - velocidade_tartaruga)
    return tempo

def main():
    distancia_inicial = float(input("Quantos metros a tartaruga está à frente da lebre? "))
    
    velocidade_tartaruga = 1  
    velocidade_lebre = 10
    
    tempo_para_alcance = calcular_tempo_para_alcance(distancia_inicial, velocidade_tartaruga, velocidade_lebre)
    
    print(f"A lebre alcançará a tartaruga em aproximadamente {tempo_para_alcance:.0f} minutos.")

if __name__ == "__main__":
    main()
