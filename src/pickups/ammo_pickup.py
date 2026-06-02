from .pickup import Pickup
from ..settings import AMMO_PICKUP_AMOUNT


class AmmoPickup(Pickup):
    IMAGE_PATH = "assets/pickups/ammo.png"
    PICKUP_NAME = "ammo"
    FRAME_WIDTH = 16
    FRAME_HEIGHT = 15
    ANIMATED = False

    def apply(self, player):
        player.add_ammo(AMMO_PICKUP_AMOUNT)
        self.kill()