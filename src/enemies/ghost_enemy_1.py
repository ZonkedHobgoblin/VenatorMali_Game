# enemies/enemy_shooter.py
from __future__ import annotations
import pygame

from ..utils import load_image, slice_sprite_sheet_row
from ..animation import Animation
from ..weapons.pistol import Pistol
from .enemy import Enemy


class Ghost1(Enemy):
    """Stationary shooter that fires towards the player."""

    def __init__(self, pos: tuple[int, int]):
        super().__init__()

        idle_sheet = load_image("ghost1_idle.png")
        die_sheet = load_image("ghost1_die.png")
        attack_sheet = load_image("ghost1_attack.png")

        idle_frames = slice_sprite_sheet_row(
            idle_sheet, row=0, frame_w=20, frame_h=31,
            num_frames=4, stride_x=24, start_x=2, start_y=0, clamp=True
        )
        
        dying_frames = slice_sprite_sheet_row(
            die_sheet, row=0, frame_w=16, frame_h=31,
            num_frames=4, stride_x=21, start_x=22, start_y=0, clamp=True
        )

        self.idle_anim = Animation(idle_frames, frame_duration=0.25, loop=True)
        self.die_anim = Animation(dying_frames, frame_duration=0.25, loop=False)
        self.current_anim = self.idle_anim

        self.image = self.current_anim.image
        self.rect = self.image.get_rect(topleft=pos)

        self.health = 20

        # weapon tuning
        self.weapon = Pistol()
        self.weapon.cooldown = 0.9  # slower than player

        # Optional: only shoot if player is roughly in range
        self.range_px = 520
    

    def update(self, dt: float, level, player, enemy_bullets: pygame.sprite.Group) -> None:
        direction = self.face_player(player)

        self.apply_anim(dt)

        self.weapon.update(dt)

        dx = abs(player.rect.centerx - self.rect.centerx)
        if dx > self.range_px:
            return

        if self.weapon.can_shoot():
            muzzle = pygame.Vector2(
                self.rect.centerx + 16 * direction,
                self.rect.centery + 4
            )
            self.weapon.shoot(enemy_bullets, muzzle, direction)
        
        
