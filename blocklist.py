from dataclasses import dataclass
from block import Block

@dataclass
class BlockList:
    block_type: str
    block_list: list

p = BlockList('grass', [1,2,3])
p.block_list.append(3)
print(p)