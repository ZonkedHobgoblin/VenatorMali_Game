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
            "jump": pygame.K_SPACE, # list support so it can be W and Space?
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
    
    
    def update_start_frame(self):
        """
        We call this at the start of each frame
        Basically clears all the inputs that last 1 frame (so not the held input)
        """
        for action in self.bindings:
            self.pressed[action] = False
            self.released[action] = False
            
    def process_event(self, event: pygame.event.Event):
        """
        Updates bind states from passed events by GM
        """
        if event.type == pygame.KEYDOWN:
            for action, key in self.bindings.items():
                if event.key == key:
                    self.pressed[action] = True
                    self.held[action] = True
                    
        elif event.type == pygame.KEYUP:
            for action, key in self.bindings.items():
                if event.key == key:
                    self.held[action] = False
                    self.released[action] = True
                    
    # util functions
    def is_pressed(self, action: str) -> bool:
        return self.pressed.get(action, False)
    
    def is_held(self, action: str) -> bool:
        return self.held.get(action, False)