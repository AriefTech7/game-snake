import pygame
import random
import math
from settings import *

class Menu:
    def __init__(self, screen, scoreboard):
        self.screen = screen
        self.scoreboard = scoreboard
        self.running = True
        self.start_game = False
        
        # Animasi background - partikel mengambang
        self.bg_particles = []
        for _ in range(50):
            self.bg_particles.append({
                'x': random.randint(0, SCREEN_WIDTH),
                'y': random.randint(0, SCREEN_HEIGHT),
                'size': random.randint(2, 5),
                'speed': random.uniform(0.5, 2),
                'opacity': random.randint(50, 150)
            })
            
        # Tombol
        self.buttons = [
            {
                'text': 'START GAME',
                'rect': pygame.Rect(SCREEN_WIDTH//2 - 120, 320, 240, 50),
                'color': COLOR_SNAKE_HEAD,
                'hover_color': (100, 255, 180),
                'action': self._start
            },
            {
                'text': 'QUIT',
                'rect': pygame.Rect(SCREEN_WIDTH//2 - 120, 390, 240, 50),
                'color': COLOR_FOOD_NORMAL,
                'hover_color': (255, 120, 120),
                'action': self._quit
            }
        ]
        
        # Animasi judul
        self.title_offset = 0
        self.snake_decor = []  # Ular dekorasi di background menu
        
    def _start(self):
        self.start_game = True
        self.running = False
        
    def _quit(self):
        self.start_game = False
        self.running = False
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self._start()
                    return True
                if event.key == pygame.K_ESCAPE:
                    self._quit()
                    return False
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Klik kiri
                    mouse_pos = event.pos
                    for btn in self.buttons:
                        if btn['rect'].collidepoint(mouse_pos):
                            btn['action']()
                            return True
        return True
        
    def update(self):
        # Update animasi partikel background
        for p in self.bg_particles:
            p['y'] -= p['speed']
            if p['y'] < -10:
                p['y'] = SCREEN_HEIGHT + 10
                p['x'] = random.randint(0, SCREEN_WIDTH)
                
        # Update animasi judul (floating effect)
        self.title_offset += 0.03
        
    def _draw_glow_text(self, text, font, color, pos, intensity=3):
        """Gambar teks dengan efek glow"""
        # Glow layers
        for i in range(intensity, 0, -1):
            alpha = 80 - (i * 20)
            glow_surf = font.render(text, True, color)
            glow_surf.set_alpha(alpha)
            offset = i * 2
            for dx, dy in [(-1,-1), (-1,1), (1,-1), (1,1), (0,0)]:
                self.screen.blit(glow_surf, 
                    (pos[0] + dx*offset, pos[1] + dy*offset))
        
        # Teks utama
        main_surf = font.render(text, True, COLOR_HIGHLIGHT)
        self.screen.blit(main_surf, pos)
        
    def draw(self):
        self.screen.fill(COLOR_BG)
        
        # Gambar partikel background
        for p in self.bg_particles:
            surf = pygame.Surface((p['size']*2, p['size']*2), pygame.SRCALPHA)
            pygame.draw.circle(surf, (100, 255, 150, p['opacity']), 
                             (p['size'], p['size']), p['size'])
            self.screen.blit(surf, (int(p['x']), int(p['y'])))
            
        # Gambar grid tipis
        for x in range(0, SCREEN_WIDTH, CELL_SIZE * 2):
            pygame.draw.line(self.screen, (20, 20, 40), (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, CELL_SIZE * 2):
            pygame.draw.line(self.screen, (20, 20, 40), (0, y), (SCREEN_WIDTH, y))
            
        # JUDUL dengan animasi floating
        float_y = int(math.sin(self.title_offset) * 8)
        
        # Shadow/glow judul
        title_text = "NEON SNAKE"
        title_surf = FONT_LARGE.render(title_text, True, COLOR_SNAKE_HEAD)
        title_rect = title_surf.get_rect(center=(SCREEN_WIDTH//2, 120 + float_y))
        
        # Glow effect
        for i in range(3, 0, -1):
            glow = FONT_LARGE.render(title_text, True, COLOR_SNAKE_HEAD)
            glow.set_alpha(100 - i*25)
            self.screen.blit(glow, title_rect.move(i*2, i*2))
            self.screen.blit(glow, title_rect.move(-i*2, -i*2))
            
        self.screen.blit(title_surf, title_rect)
        
        # Subtitle
        sub_text = "PYGAME EDITION"
        sub_surf = FONT_MEDIUM.render(sub_text, True, (150, 150, 180))
        sub_rect = sub_surf.get_rect(center=(SCREEN_WIDTH//2, 170 + float_y))
        self.screen.blit(sub_surf, sub_rect)
        
        # High Score
        hs_text = f"HIGH SCORE: {self.scoreboard.high_score}"
        hs_surf = FONT_MEDIUM.render(hs_text, True, COLOR_FOOD_GOLD)
        hs_rect = hs_surf.get_rect(center=(SCREEN_WIDTH//2, 230))
        self.screen.blit(hs_surf, hs_rect)
        
        # Instruksi
        inst_text = "Use Arrow Keys or WASD to move"
        inst_surf = FONT_SMALL.render(inst_text, True, (120, 120, 140))
        inst_rect = inst_surf.get_rect(center=(SCREEN_WIDTH//2, 270))
        self.screen.blit(inst_surf, inst_rect)
        
        # Tombol
        mouse_pos = pygame.mouse.get_pos()
        for btn in self.buttons:
            rect = btn['rect']
            is_hover = rect.collidepoint(mouse_pos)
            
            # Warna berubah saat hover
            color = btn['hover_color'] if is_hover else btn['color']
            
            # Glow saat hover
            if is_hover:
                glow_rect = rect.inflate(10, 10)
                glow = pygame.Surface((glow_rect.width, glow_rect.height), pygame.SRCALPHA)
                pygame.draw.rect(glow, (*color[:3], 100), glow_rect, border_radius=12)
                self.screen.blit(glow, glow_rect)
            
            # Tombol utama
            pygame.draw.rect(self.screen, color, rect, border_radius=10)
            pygame.draw.rect(self.screen, COLOR_HIGHLIGHT, rect, width=2, border_radius=10)
            
            # Teks tombol
            text_surf = FONT_MEDIUM.render(btn['text'], True, COLOR_BG)
            text_rect = text_surf.get_rect(center=rect.center)
            self.screen.blit(text_surf, text_rect)
            
            # Icon panah saat hover
            if is_hover:
                arrow = FONT_MEDIUM.render("<-", True, COLOR_HIGHLIGHT)
                self.screen.blit(arrow, (rect.right + 10, rect.centery - 12))
        
        # Footer
        footer = FONT_SMALL.render("Press ENTER to start | ESC to quit", True, (80, 80, 100))
        footer_rect = footer.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 30))
        self.screen.blit(footer, footer_rect)
        
        pygame.display.flip()
        
    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            if not self.handle_events():
                return False
                
            self.update()
            self.draw()
            clock.tick(FPS)
            
        return self.start_game
