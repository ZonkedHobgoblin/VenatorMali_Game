# enemies/enemy_shooter.py
from __future__ import annotations
import pygame

from ..utils import load_image, slice_sprite_sheet_row
from ..animation import Animation
from ..weapons.pistol import Pistol
from .. import settings
from .enemy import Enemy


class Ghost3(Enemy):

    def __init__(self, pos: tuple[int, int]):
        super().__init__()

        idle_sheet = load_image("ghost3_idle.png")
        die_sheet = load_image("ghost3_die.png")

        idle_frames = slice_sprite_sheet_row(
            idle_sheet, row=0, frame_w=16, frame_h=34,
            num_frames=5, stride_x=19, start_x=3, start_y=0, clamp=True
        )
        
        dying_frames = slice_sprite_sheet_row(
            die_sheet, row=0, frame_w=19, frame_h=34,
            num_frames=5, stride_x=19, start_x=3, start_y=0, clamp=True
        )

        self.state = "IDLE"
        self.idle_anim = Animation(idle_frames, frame_duration=0.25, loop=True)
        self.die_anim = Animation(dying_frames, frame_duration=0.025, loop= False)
        self.current_anim = self.idle_anim

        self.image = self.current_anim.image
        self.rect = self.image.get_rect(topleft=pos)

        self.health = 20
        self.facing = 1

        # weapon tuning
        self.weapon = Pistol()
        self.weapon.cooldown = 0.6 

        self.range_px = 520


    def change_state(self, new_state: str, new_anim: Animation):
        if self.state != new_state:
            self.state = new_state
            self.current_anim = new_anim
            if hasattr(self.current_anim, 'reset'):
                self.current_anim.reset()
                
    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0 and self.state != "DIE":
            self.change_state("DIE", self.die_anim)


    def update(self, dt: float, level, player, enemy_bullets: pygame.sprite.Group) -> None:
        if self.state != "DIE":
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


        self.apply_anim(dt)
        if self.state == "DIE" and getattr(self.current_anim, 'finished', False):
            self.kill()