import pygame
import sys
import random

#Inicialização do Pygame
pygame.init()

#Definições de janela
window_size=(400,400)
window=pygame.display.set_mode()window_size
pygame.display.set_caption("Jogo Snake")

#Cores
white=(255,255,255)
black=(0,0,0)_
green=(0,255,0)

#Tamanho do bloco e velocidade
block_size=20
speed=10

#Relógio para controle de FPS
clock=pygame.time.Clock()

#Função para desenhar a cobra
def game():
    snake=[[100,100]]
    direction=[block_size,0]
    food=[random.randrange(0,window_size[0]-block_size,block_size),
         [random.randrange(0,window_size[1]-block_size,block_size)]

while True:
for event in pygame.event.get():
    if event,type==pygame.KEYDOWN: