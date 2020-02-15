import numpy as np
import gridWorld
import graphics 
import time
import random


# Create our grid
length = 10
width = 10
goalX = 2
goalY = 3
currentX = 6
currentY = 6
myGrid = gridWorld.grid(length, width, currentX, currentY, goalX, goalY)

discount = 0.95
learning_rate = 0.8

numGames = 100

# Describe here

# Q_Table is a tensor!
Q_Table = np.zeros( (length, width, 4) )

# Prior state tracking
currentY_p = currentY
currentX_p = currentX

for gam_num in range(numGames):

    for i in range(100):
        myGrid.render()
    
        action = np.argmax(Q_Table[currentY, currentX, :] +  np.random.randn(1, 4) * (1.0/ ( i + 1.0 ) ) ) 
    
        current_reward, isOver, currentX, currentY = myGrid.step(action)
    
        Q_Table[currentY, currentX, action] = Q_Table[currentY, currentX, action] + ( (learning_rate) * ( discount * np.max(Q_Table[currentY, currentX, :] )  - Q_Table[currentY_p, currentX_p, action] ) )
    

        if ( isOver == True ):
            print("Game Over")
            myGrid.reset()
            i = 101

    
        # time.sleep(0.2)


while(1):
    myGrid.render()
    pass






