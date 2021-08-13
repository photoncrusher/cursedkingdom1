import pygame
from constants import *
import sys
from player import Player
class Game:
    def __init__(self, map) -> None:
        self.isPaused = False
        pygame.display.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.map = map
        self.player = Player()
    
    def draw(self):
        self.clock.tick(FRAMERATE)
        while True:
            self.screen.fill(CYAN_BR)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                self.player.check_move(event)
            next_chunk = self.map.get_4_chunk(self.player.position)
            current_chunk = [next_chunk[1], next_chunk[2], next_chunk[3]]
            self.map.draw(self.screen, self.player.position, next_chunk)
            self.player.load(self.screen, current_chunk, self.map.preloadedList)
            pygame.display.flip()