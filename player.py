from constants import *
import pygame

class Player:
    
    def __init__(self) -> None:
        # PLAYER BLOCK CONFIGURATOR
        self.rect = pygame.Rect(0,0,BLOCK_SIZE, BLOCK_SIZE)
        self.rect.center = (WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2)
        self.image = PLAYER1
        self.imageL = self.image
        self.imageR = pygame.transform.flip(self.imageL, True, False)
        self.image = self.imageL

        # LOGICAL AND PHYSICS CONF :[x, y]
        self.position = [0, -100]
        self.direction = [0,0]
        self.v = [0,0]
        self.collide = [0,0,0,0]
        self.mine_dir = 0
        self.block_collide = []
        self.jumping = 0
        

    def check_collide(self, block, position):
        if block.passAble == 0:
            limitx = block.rect.centery - position[1]
            limity = block.rect.centerx - position[0]
            if abs(limity) < BLOCK_SIZE - 4:
                if limitx <= BLOCK_SIZE and limitx > 0:
                    self.collide[1] = 1
                if - limitx  <=  BLOCK_SIZE and - limitx > 0:
                    self.collide[0] = 1
            if abs(limitx) < BLOCK_SIZE:
                if limity <= BLOCK_SIZE and limity > 0:
                    self.collide[3] = 1
                if -limity <= BLOCK_SIZE and -limity > 0:
                    self.collide[2] = 1

    def check_move(self, event):
        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_RIGHT:
                self.direction[0] = 1
            if event.key == pygame.K_LEFT:
                self.direction[0] = -1
            if event.key == pygame.K_UP:
                if self.jumping == 0:
                    self.jumping = 20
            if event.key == pygame.K_SPACE:
                self.mine_dir = 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.direction[0] = 0
            if event.key == pygame.K_LEFT:
                self.direction[0] = 0
            if event.key == pygame.K_UP:
                self.direction[1] = 0
            if event.key == pygame.K_SPACE:
                self.mine_dir = 0
    
    def physics_cal(self, preloadedList, chunk):
        if self.jumping != 0:
            self.jumping -= 1
            self.direction[1] = -2
        if self.jumping == 0:
            self.direction[1] = 0
        

        self.v[0] = min(max(self.v[0] + self.direction[0], -2), 2) * int(self.direction[0] != 0)
        self.v[1] = min(max(self.v[1] + self.direction[1], -6), 4) * int(self.direction[1] != 0)
        
        gravity = 1
        self.v[1] += gravity

        if self.v[0]>0:
            self.image = self.imageL
        if self.v[0]<0:
            self.image = self.imageR

        next_pos_x = self.position[0] + self.v[0]
        next_pos_y = self.position[1] + self.v[1]

        # check collision
        self.collide = [0,0,0,0]
        self.block_collide = []
        for c in chunk:
            for p in range(0,len(preloadedList)):
                if c in preloadedList[p]:
                    for block in preloadedList[p][c]:
                        self.check_collide(block, [next_pos_x, next_pos_y])
                        if self.collide[1] == 1 and self.block_collide == []:
                            self.block_collide.append([p,c,block])
        # count v coll
        v_down = min(self.v[1] , self.v[1]*int(self.collide[1] == 0))
        v_y = max(v_down, v_down*int(self.collide[0] == 0))

        v_left = min(self.v[0] , self.v[0]*int(self.collide[3] == 0))
        v_x = max(v_left, v_left*int(self.collide[2] == 0))

        self.check_mine(preloadedList)

        # tinh lai pos theo v
        self.position[0] += v_x
        self.position[1] += v_y
    
    def check_mine(self, preloadedList):
        if self.mine_dir == 1:
            if self.block_collide != []:
                a = self.block_collide[0][0]
                b = self.block_collide[0][1]
                c = self.block_collide[0][2]
                preloadedList[a][b].remove(c)
        


    def load(self, screen, chunk, preloadedList):
        screen.blit(self.image, self.rect)
        self.physics_cal(preloadedList, chunk)