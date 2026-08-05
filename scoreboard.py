import pygame
import os
from settings import *

DATA_FILE = "data.txt"

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = self._load_high_score()
        self.level = 1
        
    def _load_high_score(self):
        if os.path.exists(DATA_FILE):
            try:
                with open(DATA_FILE, "r") as f:
                    return int(f.read().strip())
            except:
                return 0
        return 0
        
    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(DATA_FILE, "w") as f:
                f.write(str(self.high_score))
                
    def add_score(self, value):
        self.score += value
        # Naik level setiap 5 poin
        self.level = 1 + self.score // 5
        
    def reset(self):
        self.save_high_score()
        self.score = 0
        self.level = 1
        
    def get_speed(self):
        """Kecepatan bertambah tiap level"""
        speed = BASE_SPEED - (self.level - 1) * 8
        return max(MIN_SPEED, speed)
        
    def draw(self, surface):
        # Panel skor di atas
        panel = pygame.Rect(0, 0, SCREEN_WIDTH, 50)
        pygame.draw.rect(surface, (20, 20, 40), panel)
        pygame.draw.line(surface, COLOR_GRID, (0, 50), (SCREEN_WIDTH, 50), 2)
        
        # Teks skor
        score_text = FONT_MEDIUM.render(f"SCORE: {self.score}", True, COLOR_TEXT)
        high_text = FONT_MEDIUM.render(f"BEST: {self.high_score}", True, (180, 180, 180))
        level_text = FONT_MEDIUM.render(f"LEVEL: {self.level}", True, COLOR_FOOD_GOLD)
        
        surface.blit(score_text, (20, 10))
        surface.blit(high_text, (160, 10))
        surface.blit(level_text, (SCREEN_WIDTH - 120, 12))
        
    def draw_game_over(self, surface):
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        surface.blit(overlay, (0, 0))
        
        texts = [
            (FONT_LARGE.render("GAME OVER", True, COLOR_FOOD_NORMAL), -40),
            (FONT_MEDIUM.render(f"Score: {self.score}", True, COLOR_TEXT), 10),
            (FONT_SMALL.render("Press SPACE to restart", True, (200, 200, 200)), 50),
            (FONT_SMALL.render("Press ESC to quit", True, (150, 150, 150)), 75)
        ]
        
        for text, offset in texts:
            rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + offset))
            surface.blit(text, rect)
