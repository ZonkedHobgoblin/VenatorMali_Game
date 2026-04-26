"""
PhysicsManager.py - 20/04/26
Physics engine for scene manager
"""
class PhysicsManager:
    def __init__(self, scene_objects: list, gravity: float, dampening: float, ):
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
            start_pos = phys_obj.pos
            vel = phys_obj.vel
            accel = phys_obj.accel
            
            
        
    
    def _check_collisions(self) -> None:
        """Make sure collisions are handled"""
        pass