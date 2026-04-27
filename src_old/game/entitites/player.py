"""
player.py - 19/04/26
"""
from game.entitites.game_object import GameObject

class Player(GameObject):
    def __init__(self, x:float, y:float, width:float, height:float):
        super().__init__(x, y, width, height)
        self.tags.append("player", "damageable", "actor", "physics_object")
        
        # self.sprite_handler (setup stuff)
        self.health = None
        self.inventory = None