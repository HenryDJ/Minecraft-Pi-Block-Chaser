from mcpi import minecraft
# Imports the minecraft module from the mcpi module.

import time
import random

mc = minecraft.Minecraft.create()
# Saves from typing minecraft.Minecraft.create every time.

bedrock = 7
air = 0
# Sets variables to make it easier to remember the blocks.

blockType = bedrock
# Sets the original block type.

blockSpeed = 1.75
# Sets the block speed per second.

x, y, z = mc.player.getTilePos()
blockX = x
blockZ = z
blockY = y+10

time.sleep(3)
while True: # A forever loop
    x, y, z  =  mc.player.getTilePos()
    # Unpacks the getPos() module into x, y, and z.
    mc.setBlock(blockX, blockY, blockZ, air)
    if x > blockX:
        blockX = blockX + 1
        if not mc.getBlock(blockX, blockY, blockZ) == air and not mc.getBlock(blockX, blockY, blockZ) == 95:
            blockType = mc.getBlock(blockX, blockY, blockZ)
    elif x < blockX:
        blockX = blockX - 1
        if not mc.getBlock(blockX, blockY, blockZ) == air and not mc.getBlock(blockX, blockY, blockZ) == 95:
            blockType = mc.getBlock(blockX, blockY, blockZ)
    if z > blockZ:
        blockZ = blockZ + 1
        if not mc.getBlock(blockX, blockY, blockZ) == air and not mc.getBlock(blockX, blockY, blockZ) == 95:
            blockType = mc.getBlock(blockX, blockY, blockZ)
    elif z < blockZ:
        blockZ = blockZ - 1
        if not mc.getBlock(blockX, blockY, blockZ) == air and not mc.getBlock(blockX, blockY, blockZ) == 95:
            blockType = mc.getBlock(blockX, blockY, blockZ)
    if y > blockY:
        blockY = blockY + 1
        if not mc.getBlock(blockX, blockY, blockZ) == air and not mc.getBlock(blockX, blockY, blockZ) == 95:
            blockType = mc.getBlock(blockX, blockY, blockZ)
    elif y < blockY:
        blockY = blockY - 1
        if not mc.getBlock(blockX, blockY, blockZ) == air and not mc.getBlock(blockX, blockY, blockZ) == 95:
            blockType = mc.getBlock(blockX, blockY, blockZ)
        
    # Checks if the x, y and z are more or less than the blockX, blockY and blockZ and adjusts them accordingly.
    mc.setBlock(blockX, blockY, blockZ, blockType)
    time.sleep(1 / blockSpeed)
