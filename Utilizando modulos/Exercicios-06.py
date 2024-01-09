#Faça um programa em pytho que abra e reproduza o áudio de um arquivo MP3
import pygame
pygame.mixer.init()
pygame.mixer.music.load('Mc Rogê feat. G Talibã - Saquarema (DJ Meek e DJ Boladinho)')
pygame.mixer.music.play()
print = input('Digite algo para cancelar a musica:')