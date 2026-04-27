"""
SceneManager.py - 26/04/26
"""
import pygame
from game.managers.PhysicsManager import PhysicsManager
from game.entitites.game_object import GameObject


class SceneManager:
    def __init__(self):
        self.level_manager = None
        self.physics_manager = PhysicsManager()
        self.camera_manager = None
        self.ui_manager = None
        self.audio_manager = None
        
        
        # test stuff VVV
        self.TestObject = GameObject(0, 440, 100, 50, 50)
        self.TestObject.tags.append("physics_object")
        self.TestObject.accel += pygame.math.Vector2(5000, 0)
        
        self.TestObject2 = GameObject(0, 854, 100, 50, 50)
        self.TestObject2.tags.append("physics_object")
        self.TestObject2.accel += pygame.math.Vector2(-5000, 0)
        
        self.scene_objs = [self.TestObject, self.TestObject2]
        
        self.physics_manager.physics_dampening = pygame.math.Vector2(0.05, 0.05)
        #self.physics_manager.physics_gravity = 900.0
        self.physics_manager.update_phys_objs(self.scene_objs)
    
    
    #test also  
    def update(self, dt):
        self.physics_manager.calculate_phys(dt)
        print(self.scene_objs[0].vel)
        