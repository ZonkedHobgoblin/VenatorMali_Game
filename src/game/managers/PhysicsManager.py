"""
PhysicsManager.py - 20/04/26
Physics engine for scene manager
"""


class PhysicsManager:
    def _init__(self, scene_objects: list, gravity: int, dampening: int, ):
        self.physics_objects = []
        self.physics_objects.append(scene_objects)
        self.physics_gravity = gravity
        self.physics_dampening = dampening
        
        
    def get_phys_objs(self) -> list :
        return self.physics_objects