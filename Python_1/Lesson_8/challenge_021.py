import pygame

pygame.init()
pygame.mixer.music.load("helloMonday.mp3")
pygame.mixer.music.play()
pygame.event.wait()