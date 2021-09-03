import pygame
from constants import *
import sys
from player import Player
from ui import inventoryBar
from gameLogical import gameLogical
class Game:
    def __init__(self, map, ui, ev, gw) -> None:
        self.isPaused = False
        pygame.display.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.map = map
        self.player = Player()
        self.bar = inventoryBar((WINDOW_SIZE[0]/2,WINDOW_SIZE[1]/10*9))
        self.gameLogical = gameLogical(ui,ev, gw)
        self.gameWindow = gw

    def draw(self):
        self.clock.tick(FRAMERATE)
        # self.gameLogical.render()
        while True:
            self.gameLogical.gameWindow.render()
            # self.gameLogical.gameScene.render()
            # self.gameLogical.gamePlayer.render(self.gameLogical.gameScene.block_group)
            self.gameLogical.userInterface.render()
            self.gameLogical.get_Logical()
            # self.screen.blit(BACKGROUND,(0,0,WINDOW_SIZE[0], WINDOW_SIZE[1]))
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         sys.exit()
            #     self.player.check_move(event)
            # next_chunk = self.map.get_4_chunk(self.player.position)
            # current_chunk = [next_chunk[1], next_chunk[2], next_chunk[3]]
            # self.map.draw(self.screen, self.player.position, next_chunk)
            # self.player.load(self.screen, current_chunk, self.map.preloadedList)
            # self.bar.draw(self.screen)
            # pygame.display.flip()