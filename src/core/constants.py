import platform
from pathlib import Path

class Env:
    OS_NAME = platform.system()
    # src folder
    SCRIPT_PATH = Path(__file__).resolve().parent.parent
class Meta:
    GAME_VERSION = "0.0.1"