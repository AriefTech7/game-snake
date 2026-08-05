import pygame
import random
import math  
from settings import *

class Food:
    def __init__(self, snake_body):
        self.type = "normal"
        self.position = self._random_position(snake_body)
        self.animation_offset = 0
        self.animation_speed = 0.15
        
    def _random_position(self, snake_body):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), 
                   random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_body:
                return pos
                
    def refresh(self, snake_body):
        rand = random.random()
        if rand < 0.1:
            self.type = "gold"
        elif rand < 0.2:
            self.type = "slow"
        else:
            self.type = "normal"
        self.position = self._random_position(snake_body)
        
    def update(self):
        self.animation_offset += self.animation_speed
        if self.animation_offset > 3.14 * 2:
            self.animation_offset = 0
            
    def draw(self, surface):
        x = self.position[0] * CELL_SIZE
        y = self.position[1] * CELL_SIZE
        center = (x + CELL_SIZE // 2, y + CELL_SIZE // 2)
        
        if self.type == "gold":
            color = COLOR_FOOD_GOLD
            glow_color = (255, 200, 50, 100)
            radius = 8
        elif self.type == "slow":
            color = COLOR_FOOD_SLOW
            glow_color = (100, 150, 255, 100)
            radius = 8
        else:
            color = COLOR_FOOD_NORMAL
            glow_color = (255, 100, 100, 80)
            radius = 6
            
        # PERBAIKAN: math.sin bukan pygame.math.sin
        pulse = abs(math.sin(self.animation_offset)) * 3
        
        glow = pygame.Surface((CELL_SIZE + 10, CELL_SIZE + 10), pygame.SRCALPHA)
        pygame.draw.circle(glow, glow_color, 
                          (CELL_SIZE // 2 + 5, CELL_SIZE // 2 + 5), 
                          radius + pulse + 4)
        surface.blit(glow, (x - 5, y - 5))
        
        pygame.draw.circle(surface, color, center, radius + pulse)
        pygame.draw.circle(surface, COLOR_HIGHLIGHT, center, radius // 2)
        
    def get_score_value(self):
        if self.type == "gold":
            return 5
        elif self.type == "slow":
            return 2
        return 1
        
    def get_speed_modifier(self):
        if self.type == "slow":
            return 1.5
        return 1.0
