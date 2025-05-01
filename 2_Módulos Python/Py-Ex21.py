#Autor: Lucas Gabriel dos Santos Lima
#Data: 03-08-2024
#Objetivo: Crie um programa em  Python que abra e reproduza o áudio de um arquivo MP3.

#Importa a biblioteca pygame com as funçoes das linhas 7-9 e 11
import pygame
pygame.init()
pygame.mixer.music.load('elevador.MP3')
pygame.mixer.music.play()
input()
pygame.event.wait()

# ✟