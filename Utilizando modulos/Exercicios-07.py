#Faça um programa que reproduza um audio em MP3
import pygame
import os

pygame.init()

# Obtenha o caminho absoluto para o arquivo de música
file_path = os.path.join(os.getcwd(), "mp3.mp3")

# Carregue e reproduza o arquivo de música
pygame.mixer.music.load(file_path)
pygame.mixer.music.play()

# Aguarde o término da música
pygame.event.wait()