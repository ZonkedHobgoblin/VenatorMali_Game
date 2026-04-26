"""
game_object.py - 26/04/26
Base game object class for other scripts to use
"""
import pygame
class GameObject:
    def __init__(self, object_id:int, x:float, y:float, width:float, height:float):
        # Rendering stuff
        self.sprite_handler = None # needs to pass json file or path to handler for sprite sheet
        self.z_index = 0 # 0 for background, 1 for the same index level as player, 2 for foreground
        
        self.pos = pygame.math.Vector2(x, y)
        self.vel = pygame.math.Vector2(0, 0)
        self.accel = pygame.math.Vector2(0, 0)
        self.hitbox_rect = pygame.FRect(0,0,width, height)
        self.hitbox_rect.center = (self.pos.x, self.pos.y)
        
        self.is_active = True
        # is_dead = means is this due to be deleted/destroyed
        self.is_dead = False
        
        # tags, like enemy or damagable or anything
        self.tags = []