import pygame
import random
import math  # <-- TAMBAHKAN INI
from settings import *

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = random.randint(3, 6)
        self.life = 1.0
        self.decay = random.uniform(0.02, 0.05)
        angle = random.uniform(0, 3.14 * 2)
        speed = random.uniform(1, 4)
        # PERBAIKAN: math.cos dan math.sin
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        
    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.life -= self.decay
        self.size = max(1, self.size - 0.1)
        return self.life > 0
        
    def draw(self, surface):
        alpha = int(255 * self.life)
        color_with_alpha = (*self.color[:3], alpha)
        surf = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, color_with_alpha, 
                          (self.size, self.size), self.size)
        surface.blit(surf, (int(self.x - self.size), int(self.y - self.size)))


class ParticleSystem:
    def __init__(self):
        self.particles = []
        
    def spawn_burst(self, x, y, color, count=15):
        for _ in range(count):
            self.particles.append(Particle(x, y, color))
            
    def update(self):
        self.particles = [p for p in self.particles if p.update()]
        
    def draw(self, surface):
        for particle in self.particles:
            particle.draw(surface)
            
    def clear(self):
        self.particles.clear()
