import numpy as np
import gridWorld
import graphics 
import time
import random


# Create our grid
length = 5
width = 5
goalX = 2
goalY = 3
currentX = 0
currentY = 0
myGrid = gridWorld.grid(length, width, currentX, currentY, goalX, goalY)

discount = 0.5

# Construct the Q-table
# Do I need to construct the reward function

# Search
def chooseAction(currentX, currentY):

    left = Q_Table[currentY, currentX, 0]
    right = Q_Table[currentY, currentX, 1]
    up = Q_Table[currentY, currentX, 2]
    down =  Q_Table[currentY, currentX, 3]

    index_max = 0
    if (left == right == up == down):
        index_max = random.randint(0, 3)
    else:
        index_max = np.argmax([left, right, up, down])
    
    return index_max


# Q_Table is a tensor!
Q_Table = np.zeros( (length, width, 4) )

for i in range(100):
    myGrid.render()
    
    action = chooseAction(currentX, currentY)

    current_reward, isOver, currentX, currentY = myGrid.step(action)
    
    if ( isOver == True ):
        print("Game Over")
        break

    
    time.sleep(1)


while(1):
    myGrid.render()
    pass






