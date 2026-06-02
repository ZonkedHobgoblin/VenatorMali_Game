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
from ..enemies.enemy import Enemy
from .. import settings

class Knife:
    """Knife class"""

    def __init__(
        self,
        attack_cooldown = settings.KINFE_COOLDOWN
    ):
        if attack_cooldown < 0:
            raise ValueError("cooldown must be >= 0")

        self.cooldown = attack_cooldown
        self.cooldown_timer = 0.0
        self.attack_range = settings.KNIFE_RANGE
        self.attack_damage = settings.KNIFE_DAMAGE


    def update(self, dt: float) -> None:
        if self.cooldown_timer > 0.0:
            self.cooldown_timer = max(0.0, self.cooldown_timer - dt)

    def can_attack(self) -> bool:
        return self.cooldown_timer <= 0.0

    def _start_cooldown(self) -> None:
        self.cooldown_timer = self.cooldown

    def attack(self, player: pygame.sprite.Sprite, enemies: list[Enemy]) -> None:
        """Attack the nearest enemies."""
        if not self.can_attack():
            return
        
        for enemy in enemies:
            dist_to_player = enemy.rect.centerx - player.rect.centerx
            abs_dist = abs(dist_to_player)
            y_dist = abs(player.rect.centery - enemy.rect.centery)
            
            if abs_dist < self.attack_range and y_dist < 40:
                enemy.take_damage(settings.KNIFE_DAMAGE)

        self._start_cooldown()
