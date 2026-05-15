
from .LevelManager import LevelManager


class SceneManager:
    def __init__(self):
        self.level_manager = LevelManager()
        self.physics_manager = None
        self.camera_manager = None
        self.ui_manager = None