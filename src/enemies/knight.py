from __future__ import annotations
import pygame

from ..utils import load_image, slice_sprite_sheet_row
from ..animation import Animation
from .. import settings
from .enemy import Enemy


class KnightEnemy(Enemy):
    """enemy that chases and attacks the player"""
    def __init__(self, pos: tuple[int, int]):
        super().__init__()

        # sprite sheets
        idle_sheet = load_image("knight_idle.png")
        self.anim_idle = Animation(slice_sprite_sheet_row(
            idle_sheet, row=0, frame_w=32, frame_h=32, num_frames=8, stride_x=64, start_x=0, start_y=0, clamp=True
        ), frame_duration=0.15, loop=True)

        run_sheet = load_image("knight_run.png")
        self.anim_run = Animation(slice_sprite_sheet_row(
            run_sheet, row=0, frame_w=32, frame_h=32, num_frames=5, stride_x=64, start_x=0, start_y=0, clamp=True
        ), frame_duration=0.10, loop=True)

        attack_sheet = load_image("knight_attack.png")
        self.anim_attack = Animation(slice_sprite_sheet_row(
            attack_sheet, row=0, frame_w=32, frame_h=32, num_frames=3, stride_x=64, start_x=0, start_y=0, clamp=True
        ), frame_duration=0.10, loop=False)

        die_sheet = load_image("knight_die.png")
        self.anim_die = Animation(slice_sprite_sheet_row(
            die_sheet, row=0, frame_w=32, frame_h=32, num_frames=13, stride_x=64, start_x=0, start_y=0, clamp=True
        ), frame_duration=0.15, loop=False)
        
        self.state = "RUN" # so its got 4 states: IDLE, RUN, ATTACK & DIE (idk if we bneed idle)
        self.current_anim = self.anim_run
        
        self.image = self.current_anim.image
        self.rect = self.image.get_rect(topleft=pos)

        self.pos = pygame.Vector2(self.rect.topleft)
        self.vel = pygame.Vector2(-80.0, 0.0)
        self.base_speed = 70.0

        self.health = 100
        self.on_ground = False
        self.facing = -1

        self.attack_range = 40 
        self.attack_damage = 25 

    def set_state(self, new_state: str, new_anim: Animation):
        if self.state != new_state:
            self.state = new_state
            self.current_anim = new_anim
            if hasattr(self.current_anim, 'reset'):
                self.current_anim.reset()

    def take_damage(self, amount: int) -> None:
        self.health -= amount
        if self.health <= 0 and self.state != "DIE":
            self.set_state("DIE", self.anim_die)
            self.vel.x = 0

    def update(self, dt: float, level, player) -> None:

        if self.state != "DIE":
            dist_to_player = player.rect.centerx - self.rect.centerx
            abs_dist = abs(dist_to_player)
            y_dist = abs(player.rect.centery - self.rect.centery)

            if self.state != "ATTACK":
                if abs_dist <= self.attack_range and y_dist < 40:
                    self.set_state("ATTACK", self.anim_attack)
                    self.vel.x = 0
                    self.facing = 1 if dist_to_player > 0 else -1
                else:
                    self.set_state("RUN", self.anim_run)
                    self.vel.x = self.base_speed * self.facing

            elif self.state == "ATTACK":
                self.vel.x = 0
                is_anim_finished = getattr(self.current_anim, 'finished', False) 
                
                if is_anim_finished:
                    if abs_dist <= self.attack_range and y_dist < 40:
                        if hasattr(player, 'take_damage'):
                            player.take_damage(self.attack_damage)
                    
                    self.set_state("IDLE", self.anim_idle) 

        self.vel.y += settings.GRAVITY * dt

        self.pos.x += self.vel.x * dt
        self.rect.x = round(self.pos.x)

        if level.rect_collides_solid(self.rect):
            self.pos.x -= self.vel.x * dt
            self.rect.x = round(self.pos.x)
            if self.state == "RUN":
                self.facing *= -1
                self.vel.x = self.base_speed * self.facing

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