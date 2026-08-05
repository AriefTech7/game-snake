import pygame
from settings import *

class Snake:
    def __init__(self):
        self.reset()
        
    def reset(self):
        # Posisi awal di tengah
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.body = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y)
        ]
        self.direction = (1, 0)  # Kanan
        self.next_direction = (1, 0)
        self.grow = False
        self.alive = True
        
    def change_direction(self, key):
        """Ubah arah berdasarkan input keyboard"""
        if key == pygame.K_UP or key == pygame.K_w:
            if self.direction != (0, 1):  # Cegah balik arah
                self.next_direction = (0, -1)
        elif key == pygame.K_DOWN or key == pygame.K_s:
            if self.direction != (0, -1):
                self.next_direction = (0, 1)
        elif key == pygame.K_LEFT or key == pygame.K_a:
            if self.direction != (1, 0):
                self.next_direction = (-1, 0)
        elif key == pygame.K_RIGHT or key == pygame.K_d:
            if self.direction != (-1, 0):
                self.next_direction = (1, 0)
                
    def move(self):
        """Gerakkan ular satu langkah"""
        self.direction = self.next_direction
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        # Cek tabrakan dinding
        if (new_head[0] < 0 or new_head[0] >= GRID_WIDTH or 
            new_head[1] < 0 or new_head[1] >= GRID_HEIGHT):
            self.alive = False
            return
            
        # Cek tabrakan dengan badan sendiri
        if new_head in self.body:
            self.alive = False
            return
            
        self.body.insert(0, new_head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
            
    def grow_snake(self):
        self.grow = True
        
    def draw(self, surface):
        """Gambar ular dengan efek glow"""
        for i, segment in enumerate(self.body):
            x = segment[0] * CELL_SIZE
            y = segment[1] * CELL_SIZE
            
            # Warna gradasi: kepala lebih terang
            if i == 0:
                color = COLOR_SNAKE_HEAD
                # Glow effect untuk kepala
                glow = pygame.Surface((CELL_SIZE + 6, CELL_SIZE + 6), pygame.SRCALPHA)
                pygame.draw.rect(glow, (*COLOR_SNAKE_HEAD[:3], 80), 
                               (0, 0, CELL_SIZE + 6, CELL_SIZE + 6), border_radius=6)
                surface.blit(glow, (x - 3, y - 3))
            else:
                # Badan memudar ke belakang
                fade = max(0.4, 1 - (i / len(self.body)) * 0.6)
                color = tuple(int(c * fade) for c in COLOR_SNAKE_BODY)
            
            # Gambar segmen
            rect = pygame.Rect(x + 1, y + 1, CELL_SIZE - 2, CELL_SIZE - 2)
            pygame.draw.rect(surface, color, rect, border_radius=5)
            pygame.draw.rect(surface, COLOR_SNAKE_OUTLINE, rect, width=1, border_radius=5)
            
            # Mata pada kepala
            if i == 0:
                self._draw_eyes(surface, x, y)
                
    def _draw_eyes(self, surface, x, y):
        """Gambar mata ular mengikuti arah"""
        eye_size = 4
        offset = 5
        cx, cy = x + CELL_SIZE // 2, y + CELL_SIZE // 2
        
        if self.direction == (1, 0):  # Kanan
            eyes = [(cx + 2, cy - offset), (cx + 2, cy + offset)]
        elif self.direction == (-1, 0):  # Kiri
            eyes = [(cx - 2, cy - offset), (cx - 2, cy + offset)]
        elif self.direction == (0, -1):  # Atas
            eyes = [(cx - offset, cy - 2), (cx + offset, cy - 2)]
        else:  # Bawah
            eyes = [(cx - offset, cy + 2), (cx + offset, cy + 2)]
            
        for ex, ey in eyes:
            pygame.draw.circle(surface, COLOR_HIGHLIGHT, (ex, ey), eye_size)
            pygame.draw.circle(surface, (0, 0, 0), (ex, ey), eye_size // 2)
