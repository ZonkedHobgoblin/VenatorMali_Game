"""
dev_utils.py - 17/04/26
Setup for logging system
"""
import logging
from logging.handlers import RotatingFileHandler

class LoggerSetup:
    @staticmethod
    def initialize():
        """
        Set up the logger for usage in logging over prints
        Logs to venatormali.log in same dir as main.py
        Is rotating (At 100kb size on new creation)
        """
        handler = RotatingFileHandler(
            "venatormali.log", 
            maxBytes=10**5,
            backupCount=3
            )
        
        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[handler]
        )
        logger = logging.getLogger(__name__)
        logger.info("Logger initialized")