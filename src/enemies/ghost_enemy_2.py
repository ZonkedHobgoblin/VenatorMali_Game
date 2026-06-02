from __future__ import annotations
import pygame

from ..utils import load_image, slice_sprite_sheet_row
from ..animation import Animation
from .. import settings
from .enemy import Enemy


class Ghost2(Enemy):
    """ Runner enemy that attacks the player."""

    def __init__(self, pos: tuple[int, int]):
        super().__init__()

        idle_sheet = load_image("ghost2_idle.png")
        die_sheet = load_image("ghost2_die.png")
        hit_sheet = load_image("ghost2_hit.png")

        idle_frames = slice_sprite_sheet_row(
            idle_sheet, row=0, frame_w=20, frame_h=31,
            num_frames=7, stride_x=31, start_x=8, start_y=0, clamp=True
        )
        
        dying_frames = slice_sprite_sheet_row(
            die_sheet, row=0, frame_w=27, frame_h=31,
            num_frames=7, stride_x=30, start_x=7, start_y=0, clamp=True
        )
        
        hit_frames = slice_sprite_sheet_row(
            hit_sheet, row=0, frame_w=28, frame_h= 31, 
            num_frames=7, stride_x=30, start_x= 7, start_y=0, clamp=True
        )

        self.state = "IDLE"
        self.idle_anim = Animation(idle_frames, frame_duration=0.25, loop=True)
        self.die_anim = Animation(dying_frames, frame_duration=0.25, loop=False)
        self.hit_anim = Animation(hit_frames, frame_duration=0.25, loop=False)
        self.current_anim = self.idle_anim

        self.image = self.current_anim.image
        self.rect = self.image.get_rect(topleft=pos)

        self.pos = pygame.Vector2(self.rect.topleft)
        self.vel = pygame.Vector2(-80.0, 0.0)
        self.base_speed = -80.0

        self.health = 30
        self.on_ground = False
        self.facing = 1
        
        self.attack_range = 10
        self.attack_damage = 10
        
        
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
            self.vel.x = 0
        elif self.health > 0 and self.state != "HIT":
            self.change_state("HIT", self.hit_anim)
            if self.state == "HIT":
                print("HIT")
            self.vel.x = 0

    def update(self, dt: float, level, player) -> None:
        if self.state != "DIE":
            dist_to_player = player.rect.centerx - self.rect.centerx
            abs_dist = abs(dist_to_player)
            y_dist = abs(player.rect.centery - self.rect.centery)

            if self.state != "ATTACK" and self.state != "HIT":
                if abs_dist <= self.attack_range and y_dist < 40:
                    self.state = "ATTACK"
                    self.vel.x = 0
                    self.facing = 1 if dist_to_player > 0 else -1
                else:
                    self.change_state("IDLE", self.idle_anim)
                    self.vel.x = self.base_speed * self.facing

            elif self.state == "ATTACK":
                if abs_dist <= self.attack_range and y_dist < 40:
                    if hasattr(player, 'take_damage'):
                        player.take_damage(self.attack_damage)
                self.state = "IDLE"
            
        if self.state == "HIT" and (self.current_anim, 'finished', False):
            self.change_state("IDLE", self.idle_anim)
        
        # gravity
        self.vel.y += settings.GRAVITY * dt

        # horizontal (float)
        self.pos.x += self.vel.x * dt
        self.rect.x = round(self.pos.x)

        if level.rect_collides_solid(self.rect):
            self.pos.x -= self.vel.x * dt
            self.rect.x = round(self.pos.x)
            self.vel.x *= -1
            self.facing *= -1

        # vertical (float)
        self.pos.y += self.vel.y * dt
        self.rect.y = round(self.pos.y)

        self.on_ground = False
        hits = level.get_solid_hits(self.rect)
        for tile_rect in hits:
            if self.vel.y > 0:
                self.rect.bottom = tile_rect.top
                self.vel.y = 0
                self.on_ground = True
            elif self.vel.y < 0:
                self.rect.top = tile_rect.bottom
                self.vel.y = 0
            self.pos.y = self.rect.y

        # ground probe
        if not self.on_ground:
            probe = self.rect.move(0, 1)
            if level.get_solid_hits(probe):
                self.on_ground = True

        # animation
        self.apply_anim(dt)

        # fell off world
        if self.rect.top > level.pixel_height + 200:
            self.kill()
            
        if self.state == "DIE" and getattr(self.current_anim, 'finished', False):
            self.kill()