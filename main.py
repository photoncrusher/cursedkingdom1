from game import Game
from map import Map
from player import Player
from gameEvent import gameEvent
from userInterface import userInterface
from gameWindow import gameWindow

gameWindow = gameWindow(800,600)
ui = userInterface(gameWindow)
ev = gameEvent()
map = Map(1234)
game = Game(map, ui, ev, gameWindow)

game.draw()