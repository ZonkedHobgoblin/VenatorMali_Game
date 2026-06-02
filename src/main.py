import pygame
import sys
from .game import Game

STATE_MENU = 0
STATE_PLAYING = 1

def draw_main_menu(screen, font):
    screen.fill((30, 30, 30))
    
    title_surface = font.render("venator mali", True, (255, 255, 255))
    
    screen.blit(title_surface, (200, 150))
    
    pygame.display.flip()

def main():
    game = Game()
    game.run()
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
