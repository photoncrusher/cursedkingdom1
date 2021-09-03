import pygame

WINDOW_SIZE = (800, 600)
FRAMERATE = 120
BLOCK_SIZE = 50
MAX_RUNNING_VEL = 2
MAX_FALLING_VEL = 6
UISCALE = 1

# BACKGROUD
BACKGROUND = pygame.image.load('E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\BACKGROUND.jpg')
BACKGROUND = pygame.transform.scale(BACKGROUND,WINDOW_SIZE)

# TEXTURE
PLAYER1 = pygame.image.load("E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\player1.png")
PLAYER1 = pygame.transform.scale(PLAYER1,(BLOCK_SIZE,BLOCK_SIZE))

GRASS_LAND = pygame.image.load('E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\GRASS_LAND.jpg')
GRASS_LAND = pygame.transform.scale(GRASS_LAND,(BLOCK_SIZE,BLOCK_SIZE))

STONE_BLOCK = pygame.image.load('E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\STONE_BLOCK.jpg')
STONE_BLOCK = pygame.transform.scale(STONE_BLOCK,(BLOCK_SIZE,BLOCK_SIZE))

WOOD_BLOCK = pygame.image.load('E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\WOOD_BLOCK.jpg')
WOOD_BLOCK = pygame.transform.scale(WOOD_BLOCK,(BLOCK_SIZE,BLOCK_SIZE))

LEAF_BLOCK = pygame.image.load('E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\LEAF_BLOCK.jpg')
LEAF_BLOCK = pygame.transform.scale(LEAF_BLOCK,(BLOCK_SIZE,BLOCK_SIZE))

WATER_BLOCK = pygame.image.load('E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\WATER_BLOCK.jpg')
WATER_BLOCK = pygame.transform.scale(WATER_BLOCK,(BLOCK_SIZE,BLOCK_SIZE))

SAND_BLOCK = pygame.image.load('E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\SAND_BLOCK.jpg')
SAND_BLOCK = pygame.transform.scale(SAND_BLOCK,(BLOCK_SIZE,BLOCK_SIZE))

BEDROCK_BLOCK = pygame.image.load('E:\\Cursed Kingdom I\\cursedkingdom1\\resource\\BEDROCK_BLOCK.png')
BEDROCK_BLOCK = pygame.transform.scale(BEDROCK_BLOCK,(BLOCK_SIZE,BLOCK_SIZE))