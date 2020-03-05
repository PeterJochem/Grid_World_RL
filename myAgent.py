import numpy as np
import gridWorld
import graphics 
import time
import random
# from __future__ import absolute_import, division, print_function, unicode_literals
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
# Helper libraries
import numpy as np


# Create our grid
length = 10
width =  10
goalX = 2
goalY = 3
currentX = 0
currentY = 0
myGrid = gridWorld.grid(length, width, currentX, currentY, goalX, goalY)

discount = 0.95
learning_rate = 0.80

numGames = 10000

# Describe here

# Q_Table is a tensor!
Q_Table = np.zeros( (length, width, 4) )

# Prior state tracking
currentY_p = currentY
currentX_p = currentX

for game_num in range(numGames):
    
    print(game_num)

    for i in range(10000):
        myGrid.render()
        
        # Record the true maximum action so that we can check if it has changed 
        # and if it has changed, then change the arrow in the GUI
        original_max = np.argmax(Q_Table[currentY, currentX, :] )

        # This returns the index of the max value in the numpy array
        action = np.argmax(Q_Table[currentY, currentX, :] +  np.random.randn(1, 4) * (1.0/ ( game_num + 1.0 ) ) ) 
        
        currentY_p = currentY
        currentX_p = currentX

        current_reward, isOver, currentX, currentY = myGrid.step(action)

        Q_Table[currentY_p, currentX_p, action] = Q_Table[currentY_p, currentX_p, action] + ( (learning_rate) * ( current_reward + discount * np.max(Q_Table[currentY, currentX, :] )  - Q_Table[currentY_p, currentX_p, action] ) )
    
        action_final = np.argmax(Q_Table[currentY, currentX, :] )
        
        if ( action_final != original_max ):
            # Change the arrow direction
            # changeArrow(x_grid, y_grid, direction) 
            myGrid.changeArrow( currentX, currentY, action_final  )


        if ( isOver == True ):
            # print("Game Over")
            myGrid.reset()
            break

    
        # time.sleep(0.2)







