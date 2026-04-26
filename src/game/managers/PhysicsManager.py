"""
PhysicsManager.py - 26/04/26
Physics engine for scene manager
"""
import pygame
class PhysicsManager:
    def __init__(self, scene_objects: list, gravity: float = -9.81, dampening: float = 0.0):
        self.physics_objects = [] # full of object IDs, should get each object and their pos from scene man using the id
        self.physics_objects.extend(scene_objects)
        self.physics_gravity = gravity
        self.physics_dampening = dampening
        
        
    def get_phys_objs(self) -> list :
        return self.physics_objects
    
    def update_phys_objs(self, scene_objects: list) -> None:
        self.physics_objects.clear()
        self.physics_objects.extend(scene_objects)
        
    def calculate_phys(self, delta_time: float) -> None:
        self._inegrate(delta_time)
        self._check_collisions()
    
    def _inegrate(self, dt: float) -> None:
        """Handle our velocity and stuff"""
        for phys_obj in self.physics_objects:
            if "physics_object" not in phys_obj.tags:
                # Setting the hitbox pos incase static object was still moved
                phys_obj.hitbox_rect.center = (phys_obj.pos.x, phys_obj.pos.y)
                continue
            
            # Apply accel to vel
            phys_obj.accel.y += self.physics_gravity
            phys_obj.vel = phys_obj.accel * dt
            
            # Apply dampening to vel
            dampening_mult = max(0.0, 1.0 - (self.physics_dampening * dt))
            phys_obj.vel *= dampening_mult
            
            # Apply vel to pos and update positions
            phys_obj.pos += phys_obj.vel * dt
            phys_obj.accel = pygame.math.Vector2(0, 0)
            phys_obj.hitbox_rect.center = (phys_obj.pos.x, phys_obj.pos.y)
    
    def _check_collisions(self) -> None:
        """Make sure collisions are handled"""
        pass