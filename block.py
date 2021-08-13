import pygame
from constants import *

class Block:
    def __init__(self, centerx, centery) -> None:
        self.color = GRASS_BL
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 0
    
    def draw(self, screen, position):
        temp_block = pygame.Rect(0,0,BLOCK_SIZE,BLOCK_SIZE)
        temp_block.centerx = self.rect.centerx - position[0] + WINDOW_SIZE[0]/2
        temp_block.centery = self.rect.centery - position[1] + WINDOW_SIZE[1]/2
        pygame.draw.rect(screen, self.color, temp_block)

class GrassBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.color = GRASS_BL
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 0

class SandBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.color = SAND_BL
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 0

class WaterBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.color = WATER_BL
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 1
        self.hardLevel = 0

class StoneBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.color = STONE_BL
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 0

class WoodBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.color = WOOD_BL
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 1
        self.hardLevel = 0

class LeafBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.color = LEAF_BL
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 1
        self.hardLevel = 0

# class ReadyMineBlock(Block):
#     def __init__(self, centerx, centery) -> None:
#         super().__init__(centerx, centery)
#         self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
#         self.color = RED_CL
#         self.rect.centerx = centerx
#         self.rect.centery = centery
