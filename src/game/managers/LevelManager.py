class LevelManager:
    def __init__(self):
        self.current_level = None

    def load_level(self, level):
        if self.current_level:
            self.current_level.cleanup()

        self.current_level = level
        self.current_level.load()

    def update(self):
        if self.current_level:
            self.current_level.update()

    def draw(self, screen):
        if self.current_level:
            self.current_level.draw(screen)