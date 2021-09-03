from constants import *
from block import BedrockBlock, GrassBlock, StoneBlock, SandBlock, WaterBlock, WoodBlock, LeafBlock
from perlin import Perlin


class Map:
    def __init__(self, seed) -> None:
        self.seed = seed
        self.map = Perlin(seed)
        self.chunk_size = 25
        self.preloadedList = []
        self.cave_seed = abs(37218 - seed)
        self.cave_map = Perlin(self.cave_seed)
    
    def get_chunk(self):
        if self.preloadedList == []:
            return []
        else:
            chunk = []
            for preloaded in self.preloadedList:
                for key in preloaded.keys():
                    chunk.append(key)
            return chunk
    
    
    def check_load_chunk(self, chunk, next_chunk):
        if chunk == []:
            for i in next_chunk:
                self.load_chunk(i)
        else:
            for i in next_chunk:
                if i not in chunk:
                    self.load_chunk(i)
    
    def cave_generate(self, start, x, x_temp, finish, chunk):
        block_list = []
        cave_upper = str(int(hash(self.seed)))
        cave_height = 10

        top = start + cave_height + int(cave_upper[x%len(cave_upper)])
        mix = int( top%10/10 * 3) + 2
        bot = (finish - 3)
        for i in range(start + 1 , start + 1 + mix):
            tmp = GrassBlock(x_temp*BLOCK_SIZE, i*BLOCK_SIZE)
            block_list.append(tmp)
        for i in range(start+1+mix, top):
            tmp = StoneBlock(x_temp*BLOCK_SIZE, i*BLOCK_SIZE)
            block_list.append(tmp)
        if chunk % 3 == 1:
            for i in range(bot, finish):
                tmp = StoneBlock(x_temp*BLOCK_SIZE, i*BLOCK_SIZE)
                block_list.append(tmp)
        else:
            for i in range(top, finish):
                tmp = StoneBlock(x_temp*BLOCK_SIZE, i*BLOCK_SIZE)
                block_list.append(tmp)
        for i in range(finish, finish+5):
            tmp = BedrockBlock(x_temp*BLOCK_SIZE, i*BLOCK_SIZE)
            block_list.append(tmp)
        # else:
        #     for i in range(finish - 5, finish):
        #         tmp = StoneBlock(x_temp*BLOCK_SIZE, i*BLOCK_SIZE)
        #         block_list.append(tmp)
        return block_list


    def create_tree(self,h, centerx, centery):
        block_list = []
        x_temp = int(centerx/BLOCK_SIZE)
        y_temp = int(centery/BLOCK_SIZE)
        for i in range(y_temp - h, y_temp):
            block = WoodBlock(centerx, i*BLOCK_SIZE)
            block_list.append(block)
        for i in range(x_temp - 1, x_temp + 2):
            for j in range(y_temp-h-3, y_temp-h):
                block = LeafBlock(i*BLOCK_SIZE, j*BLOCK_SIZE)
                block_list.append(block) 
        return block_list
    
    def load_chunk(self, chunk):
        block_list = []
        for x in range(0, self.chunk_size):
                x_temp = self.chunk_size*chunk + x
                centerx = x_temp * BLOCK_SIZE
                centery = self.map.one(x_temp) * BLOCK_SIZE
                if centery >= 7*BLOCK_SIZE:
                    block = SandBlock(centerx, centery)
                    block_list.append(block)
                    for j in range(7, int(centery/BLOCK_SIZE)):
                        block = WaterBlock(centerx, j*BLOCK_SIZE)
                        block_list.append(block)
                else:
                    block = GrassBlock(centerx, centery)
                    block_list.append(block)
                    if x_temp % 4 ==1 and chunk % 3 != 1:
                        for tree in self.create_tree(2, centerx, centery):
                            block_list.append(tree)

                cave_block = self.cave_generate(self.map.one(x_temp), x, x_temp, 20, chunk)
                for block in cave_block:
                    block_list.append(block)

        self.preloadedList.append({chunk:block_list})
        return chunk

    def get_4_chunk(self, camera_position):
        c_p_chunk = int(camera_position[0] / (BLOCK_SIZE * self.chunk_size))
        next_chunk = [c_p_chunk-2, c_p_chunk-1, c_p_chunk, c_p_chunk + 1]
        return next_chunk

    def draw(self, screen, camera_position, next_chunk):
        chunk = self.get_chunk()
        self.check_load_chunk(chunk,next_chunk)

        if self.preloadedList != []:
            for p in self.preloadedList:
                for c in next_chunk:
                    if c in p:
                        for block in p[c]:
                            block.draw(screen, camera_position)