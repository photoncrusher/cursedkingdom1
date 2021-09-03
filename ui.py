import pygame
from constants import *

class userInterface:
    def __init__(self, center) -> None:
        pass

class inventoryBar(userInterface):
    def __init__(self, center) -> None:
        super().__init__(center)
        self.rect = pygame.Rect(0,0, 10*(BLOCK_SIZE + 10), (BLOCK_SIZE + 10))
        self.rect.center = center
    
    def draw(self, screen):
        pygame.draw.rect(screen, (220, 222, 224), self.rect, border_radius = 10)
