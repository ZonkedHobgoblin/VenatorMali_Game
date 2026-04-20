"""
player.py - 19/04/26
"""
import pygame
from game.entitites.game_object import GameObject

class Player(GameObject):
    def __init__(self, x:float, y:float, width:float, height:float):
        super().__init__(x, y, width, height)
        self.tags.append("player", "damagable", "actor")
        
        # self.sprite_handler (setup stuff)
        self.health = 0
        self.inventory = 0