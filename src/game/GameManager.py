"""
GameManager.py - 18/04/26
Initalises pygame and managers, then starts core game loop and managers
"""
import logging
import pygame
from dev import settings

logger = logging.getLogger(__name__)
class VenatorMaliGame:
    
    
    def __init__(self):
        self.scene_manager = 0
        self.camera_manager = 0
        self.input_manager = 0
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
        
        while self.running:
            
            # Handle DeltaTime
            dt = self.clock.tick(settings.FPS) / 1000.0  # convert to seconds
            dt = min(dt, 1 / 30)  # clamp if debugging causes huge dt
            
            # Temp
            self.handle_events()
            self.draw()
            
        pygame.quit()
        
            
            
    # Temp
    def draw(self) -> None:
        # START screen + UI should be fixed-size, so they draw directly to the window.
        if True:
            self.window.fill((20, 22, 30))
            pygame.display.flip()
            return
        
    def handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False