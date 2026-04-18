"""
game_object.py - 18/04/26
Base game object class for other scripts to use
"""

class GameObject:
    def __init__(self):
        self.pos = [0, 0]
        self.vel = [0, 0]
        self.hitbox = [0, 0, 0, 0]