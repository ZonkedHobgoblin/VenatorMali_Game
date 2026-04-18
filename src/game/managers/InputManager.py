"""
InputManager.py - 19/04/26
Handle and return player input
"""
import pygame

class InputManager:
    def __init__(self):
        
        # Default bindings (Just keys, as long as mouse is for UI only)
        self.bindings = {
            "move_left": pygame.K_a,
            "move_right": pygame.K_d,
            "jump": [pygame.K_SPACE, pygame.K_w],
            "attack1": pygame.K_q,
            "attack2": pygame.K_e,
            "respawn": pygame.K_r,
            "inventory": pygame.K_i,
            "pause": pygame.K_ESCAPE
        }
        
        # States for each bind
        self.pressed = {action: False for action in self.bindings}
        self.held = {action: False for action in self.bindings}
        self.released = {action: False for action in self.bindings}