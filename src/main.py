import logging
import sys
from dev.dev_utils import LoggerSetup

class VenatorMaliGame:
    
    
    def __init__(self):
        LoggerSetup.initialize()
        self.logger = logging.getLogger(__name__)
        self.logger.info("Game initialized")
    
    
    def start(self):
        pass


if __name__ == "__main__":
    try:
        game = VenatorMaliGame()
        game.start()
        
    except Exception:
        logger = logging.getLogger(__name__)
        logger.exception("Critical error occurred")
        sys.exit(1)