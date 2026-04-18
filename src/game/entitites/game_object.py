"""
game_object.py - 18/04/26
Base game object class for other scripts to use
"""
import pygame
class GameObject:
    def __init__(self, x:float, y:float, width:float, height:float):
        self.sprite_handler = None # needs to pass json file or path to handler for sprite sheet
        
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.hitbox_rect = pygame.FRect(0,0,width, height)
        self.hitbox_rect.center = (self.pos.x, self.pos.y)
        
        self.is_active = True
        # is_dead = means is this due to be deleted/destroyed
        self.is_dead = False
        
        # tags, like enemy or damagable or anything
        self.tags = []
        
    def update(self, dt:float):
        if not self.is_active:
            return
            
        self.rect.center = (self.pos.x, self.pos.y)