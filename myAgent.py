import numpy as np
import gridWorld
import graphics 


# Create our grid
length = 5
width = 5
goalX = 2
goalY = 3
myGrid = gridWorld.grid(length, width, goalX, goalY)


for i in range(3):
    myGrid.render()
    myGrid.step(1)
    
while(1):
    myGrid.render()
    pass

