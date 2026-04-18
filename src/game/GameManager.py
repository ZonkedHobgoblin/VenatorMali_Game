"""
GameManager.py - 18/04/26
Initalises pygame and managers, then starts core game loop and managers
"""
import logging
import pygame
from game.managers.InputManager import InputManager
from dev import settings

logger = logging.getLogger(__name__)
class VenatorMaliGame:
    
    
    def __init__(self):
        self.scene_manager = 0
        self.camera_manager = 0
        self.input_manager = InputManager()
        self.level_managger = 0
        self.ui_manager = 0
        self.physics_manager = 0
        self.deltatime_handler = 0
        self.event_manager = 0
    
    def start(self):
        self.running = True
        # Any further intis for managers VVVV
        
        # Load Resources VVVV
        
        # Load level / menu VVVV
        
        # Start Managers VVVV
        
        # Render Window VVVV
        self.window = pygame.display.set_mode((settings.WINDOW_WIDTH, settings.WINDOW_HEIGHT))
        pygame.display.set_caption("Venator Mali")
        self.window.fill((50,50,0))
        logger.info("Window setup complete")
        
        # pygame setup
        self.clock = pygame.time.Clock()
        logger.info("Pygame setup complete")
        self.core_loop()
        
    def core_loop(self):
        while self.running:
            
            # Handle DeltaTime
            dt = self.clock.tick(settings.FPS) / 1000.0  # convert to seconds
            dt = min(dt, 1 / 30)  # clamp if debugging causes huge dt
            
            # Handle inputs
            self.input_manager.update_start_frame()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    break
                
                self.input_manager.process_event(event)
            
            if self.input_manager.is_pressed("pause"):
                self.running = False
                break
            
            # Temp
            self.draw()
            
        pygame.quit()
            
    # Temp
    def draw(self) -> None:
        # START screen + UI should be fixed-size, so they draw directly to the window.
        if True:
            self.window.fill((20, 22, 30))
            pygame.display.flip()
            return