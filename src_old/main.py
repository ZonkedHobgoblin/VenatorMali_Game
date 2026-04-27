"""
main.py - 18/04/26
Initializes the logger system, then starts the game, then exits once game script ends
Catches exceptions, logs them and quits the script
"""
import logging
import sys
from game.GameManager import VenatorMaliGame
from dev.dev_utils import LoggerSetup

if __name__ == "__main__":
    try:
        LoggerSetup.initialize()
        logger = logging.getLogger(__name__)
        game = VenatorMaliGame()
        logger.info("Starting game")
        game.start()
        logger.info("Quiting game")
        raise SystemExit
        
    except Exception:
        logger = logging.getLogger(__name__)
        logger.exception("Critical error occurred")
        sys.exit(1)