import numpy as np
import gridWorld
import graphics 


# Create our grid
length = 10
width = 10
goalX = 7
goalY = 6
myGrid = gridWorld.grid(length, width, goalX, goalY)


for i in range(3):
    myGrid.render()
    myGrid.step(1)
    
while(1):
    pass

