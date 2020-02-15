import numpy as np
import gridWorld
import graphics 
import time

# Create our grid
length = 5
width = 5
goalX = 2
goalY = 3
myGrid = gridWorld.grid(length, width, goalX, goalY)

# Construct the Q-table
# Do I need to construct the reward function


for i in range(100):
    myGrid.render()
    
    reward, isOver = myGrid.step(2)
    
    if ( isOver == True ):
        print("game over")
        break

    
    time.sleep(1)


while(1):
    myGrid.render()
    pass

