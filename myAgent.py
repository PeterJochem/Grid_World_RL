import numpy as np
import gridWorld
import graphics 
import time
import random
import tensorflow as tf
from tensorflow import keras
import numpy as np


# Create our grid
length = 5
width =  5
goalX = 2
goalY = 1
currentX = 0
currentY = 0

# This holds all the graphics objects related to the grid
myGrid = gridWorld.grid(length, width, currentX, currentY, goalX, goalY)

# Hyper parameters
discount = 0.99
learning_rate = 0.80
epsilon = 0.1
epsilonDecay = 1.0

numGames = 10000

# Q_Table is a tensor!
Q_Table = np.zeros( (length, width, 4) )

# Prior state tracking
currentY_p = currentY
currentX_p = currentX

for game_num in range(numGames):
    
    for i in range(10000):
        myGrid.render()
        
        # Record the true maximum action so that we can check if it has changed 
        # and if it has changed, then change the arrow in the GUI
        original_max = np.argmax(Q_Table[currentY, currentX, :] )

        # This returns the index of the max value in the numpy array
        action = np.argmax(Q_Table[currentY, currentX, :] +  np.random.randn(1, 4) * (1.0/ ( game_num + 1.0 ) ) ) 
        #action = np.argmax(Q_Table[currentY, currentX, :] )

        # Explore or not?
        if ( epsilon > random.random() ):
            action = random.randrange(4)

        # This tracks the prior state
        currentY_p = currentY
        currentX_p = currentX

        # Make updates to the Q table
        current_reward, isOver, currentX, currentY = myGrid.step(action)

        Q_Table[currentY_p, currentX_p, action] = Q_Table[currentY_p, currentX_p, action] + ( (learning_rate) * ( current_reward + discount * np.max(Q_Table[currentY, currentX, :] )  - Q_Table[currentY_p, currentX_p, action] ) )
    
        action_final = np.argmax(Q_Table[currentY_p, currentX_p, :] )
        
        if ( action_final != original_max ):
            # Change the arrow direction
            #if ( (currentY_p != goalY) and (currentX_p != goalX)  ):
            myGrid.changeArrow(currentX_p, currentY_p, action_final)
            # myGrid.changeArrow(currentX, currentY, action_final)
            pass

        if ( isOver == True ):
            myGrid.reset()
            epsilon = epsilon * epsilonDecay
            break

    
