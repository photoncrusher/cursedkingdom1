import pygame
from constants import *

class Block:
    def __init__(self, centerx, centery) -> None:
        self.image = GRASS_LAND
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 0
    
    def draw(self, screen, position):
        temp_block = pygame.Rect(0,0,BLOCK_SIZE,BLOCK_SIZE)
        temp_block.centerx = self.rect.centerx - position[0] + WINDOW_SIZE[0]/2
        temp_block.centery = self.rect.centery - position[1] + WINDOW_SIZE[1]/2
        screen.blit(self.image, temp_block)

class GrassBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.image = GRASS_LAND
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 0

class SandBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.image = SAND_BLOCK
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 0

class WaterBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.image = WATER_BLOCK
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 1
        self.hardLevel = 0

class StoneBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.image = STONE_BLOCK
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 0
    
class WoodBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.image = WOOD_BLOCK
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 1
        self.hardLevel = 0

class LeafBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.image = LEAF_BLOCK
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 1
        self.hardLevel = 0

class BedrockBlock(Block):
    def __init__(self, centerx, centery) -> None:
        super().__init__(centerx, centery)
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.image = BEDROCK_BLOCK
        self.rect.centerx = centerx
        self.rect.centery = centery
        self.passAble = 0
        self.hardLevel = 1000

# class ReadyMineBlock(Block):
#     def __init__(self, centerx, centery) -> None:
#         super().__init__(centerx, centery)
#         self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
#         self.color = RED_CL
#         self.rect.centerx = centerx
#         self.rect.centery = centery
