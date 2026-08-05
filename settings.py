import pygame

# Inisialisasi pygame
pygame.init()

# Ukuran layar & grid
CELL_SIZE = 20
GRID_WIDTH = 30  # 600px
GRID_HEIGHT = 30  # 600px
SCREEN_WIDTH = CELL_SIZE * GRID_WIDTH
SCREEN_HEIGHT = CELL_SIZE * GRID_HEIGHT

# FPS
FPS = 60

# Warna tema (Dark Neon)
COLOR_BG = (15, 15, 35)
COLOR_GRID = (30, 30, 60)
COLOR_SNAKE_HEAD = (0, 255, 127)  # Spring Green
COLOR_SNAKE_BODY = (0, 200, 100)
COLOR_SNAKE_OUTLINE = (0, 100, 50)
COLOR_FOOD_NORMAL = (255, 80, 80)  # Merah coral
COLOR_FOOD_GOLD = (255, 215, 0)    # Emas (bonus)
COLOR_FOOD_SLOW = (100, 150, 255)  # Biru (slow motion)
COLOR_TEXT = (240, 240, 240)
COLOR_HIGHLIGHT = (255, 255, 255)

# Font
FONT_LARGE = pygame.font.SysFont("consolas", 40, bold=True)
FONT_MEDIUM = pygame.font.SysFont("consolas", 24)
FONT_SMALL = pygame.font.SysFont("consolas", 16)

# Kecepatan dasar (semakin kecil semakin cepat)
BASE_SPEED = 120  # milidetip per gerak
MIN_SPEED = 60
