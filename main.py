import pygame
import sys
import random
from settings import *
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from particle import ParticleSystem
from menu import Menu  # <-- IMPORT MENU


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Neon Snake - Pygame Edition")
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + 50))
        self.clock = pygame.time.Clock()
        
        # Inisialisasi objek
        self.snake = Snake()
        self.food = Food(self.snake.body)
        self.scoreboard = Scoreboard()
        self.particles = ParticleSystem()
        
        self.game_over = False
        self.move_timer = 0
        self.slow_motion_timer = 0
        self.shake_intensity = 0
        
    def show_menu(self):
        """Tampilkan start menu sebelum game"""
        menu = Menu(self.screen, self.scoreboard)
        return menu.run()
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.scoreboard.save_high_score()
                return False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    # Kembali ke menu saat ESC ditekan di game
                    return self.show_menu_from_game()
                    
                if self.game_over:
                    if event.key == pygame.K_SPACE:
                        self.restart()
                else:
                    self.snake.change_direction(event.key)
                    
        return True
        
    def show_menu_from_game(self):
        """Kembali ke menu dari dalam game"""
        self.scoreboard.save_high_score()
        menu = Menu(self.screen, self.scoreboard)
        if menu.run():
            self.restart()
            return True
        else:
            return False
        
    def restart(self):
        self.snake.reset()
        self.food.refresh(self.snake.body)
        self.scoreboard.reset()
        self.particles.clear()
        self.game_over = False
        self.move_timer = 0
        self.slow_motion_timer = 0
        
    def update(self, dt):
        if self.game_over:
            return
            
        self.food.update()
        self.particles.update()
        
        speed = self.scoreboard.get_speed()
        if self.slow_motion_timer > 0:
            speed = int(speed * 1.5)
            self.slow_motion_timer -= dt
            
        self.move_timer += dt
        if self.move_timer >= speed:
            self.move_timer = 0
            self.snake.move()
            
            if not self.snake.alive:
                self.game_over = True
                self.shake_intensity = 10
                self.scoreboard.save_high_score()
                return
                
            if self.snake.body[0] == self.food.position:
                self._eat_food()
                
    def _eat_food(self):
        score_val = self.food.get_score_value()
        self.scoreboard.add_score(score_val)
        
        x = self.food.position[0] * CELL_SIZE + CELL_SIZE // 2
        y = self.food.position[1] * CELL_SIZE + CELL_SIZE // 2 + 50
        
        if self.food.type == "gold":
            color = COLOR_FOOD_GOLD
            self.particles.spawn_burst(x, y, color, count=25)
            self.shake_intensity = 5
        elif self.food.type == "slow":
            color = COLOR_FOOD_SLOW
            self.particles.spawn_burst(x, y, color, count=20)
            self.slow_motion_timer = 5000
        else:
            color = COLOR_FOOD_NORMAL
            self.particles.spawn_burst(x, y, color, count=15)
            
        self.snake.grow_snake()
        self.food.refresh(self.snake.body)
        
    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (x, 50), (x, SCREEN_HEIGHT + 50))
        for y in range(50, SCREEN_HEIGHT + 50, CELL_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (0, y), (SCREEN_WIDTH, y))
            
    def draw(self):
        offset_x = random.randint(-self.shake_intensity, self.shake_intensity) if self.shake_intensity > 0 else 0
        offset_y = random.randint(-self.shake_intensity, self.shake_intensity) if self.shake_intensity > 0 else 0
        
        if self.shake_intensity > 0:
            self.shake_intensity = max(0, self.shake_intensity - 1)
            
        self.screen.fill(COLOR_BG)
        self.draw_grid()
        
        game_surface = self.screen.subsurface((0, 50, SCREEN_WIDTH, SCREEN_HEIGHT))
        
        self.food.draw(game_surface)
        self.snake.draw(game_surface)
        self.particles.draw(game_surface)
        
        self.scoreboard.draw(self.screen)
        
        if self.slow_motion_timer > 0:
            overlay = pygame.Surface((SCREEN_WIDTH, 30), pygame.SRCALPHA)
            overlay.fill((100, 150, 255, 60))
            self.screen.blit(overlay, (0, 50))
            slow_text = FONT_SMALL.render("SLOW MOTION ACTIVE", True, COLOR_FOOD_SLOW)
            self.screen.blit(slow_text, (SCREEN_WIDTH // 2 - 80, 55))
            
        if self.game_over:
            self.scoreboard.draw_game_over(self.screen)
            
        if offset_x or offset_y:
            shaken = self.screen.copy()
            self.screen.fill(COLOR_BG)
            self.screen.blit(shaken, (offset_x, offset_y))
            
        pygame.display.flip()
        
    def run(self):
        # TAMPILKAN MENU DULU SEBELUM GAME
        if not self.show_menu():
            pygame.quit()
            sys.exit()
            
        running = True
        while running:
            dt = self.clock.tick(FPS)
            
            running = self.handle_events()
            if not running:
                break
                
            self.update(dt)
            self.draw()
            
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
