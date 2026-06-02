# weapon.py
# Generic weapon framework with "spread burst" shots.
#
# New behaviour:
# - When a weapon fires, it spawns N bullets at once (a burst / spread).
# - Each weapon defines:
#     * burst_bullets: number of bullets spawned per trigger pull
#     * spread_deg: maximum spread angle from horizontal (degrees)
#     * cooldown: time before the weapon can fire again (seconds)
#
# Spread rule:
# - One bullet is fired horizontally (0 degrees).
# - Remaining bullets are distributed as evenly as possible across [-spread_deg, +spread_deg].
#
# This supports:
# - Pistol: burst_bullets=1, spread_deg=0, short cooldown
# - Shotgun: burst_bullets=7, spread_deg=18, longer cooldown
# - SMG: burst_bullets=3, spread_deg=8, longer cooldown than pistol, etc.

from __future__ import annotations
import math
import pygame
from .. import settings

class Knife:
    """Knife class"""

    def __init__(
        self,
        cooldown: float = 0.15,
    ):
        if cooldown < 0:
            raise ValueError("cooldown must be >= 0")

        self.cooldown = cooldown
        self.cooldown_timer = 0.0

    def update(self, dt: float) -> None:
        if self.cooldown_timer > 0.0:
            self.cooldown_timer = max(0.0, self.cooldown_timer - dt)

    def can_attack(self) -> bool:
        return self.cooldown_timer <= 0.0

    def _start_cooldown(self) -> None:
        self.cooldown_timer = self.cooldown

    def attack(self, enemies: list) -> None:
        """Attack the nearest enemies."""
        if not self.can_attack():
            return
        
        for enemy in enemies:
            enemy.take_damage(settings.KNIFE_DAMAGE)

        self._start_cooldown()
