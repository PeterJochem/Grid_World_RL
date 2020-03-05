import numpy as np
import gridWorld
import graphics 
import time
import random
# from __future__ import absolute_import, division, print_function, unicode_literals
# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras


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

# Create the neural network
Q_value = keras.Sequential([
    keras.layers.Dense(20, input_shape = (1, ) ),
    keras.layers.Dense(20, activation = 'relu'),
    keras.layers.Dense(1)
])

# Set more of the model's parameters
optimizer = tf.keras.optimizers.RMSprop(0.001)

Q_value.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])


batch_size = 100
# use np.append()
training_labels = np.array([])
input_data = np.array([])

# Get some batch of data to train on and then call the lie below
# model.fit(train_images, train_labels, epochs=10)


# Prior state tracking
currentY_p = currentY
currentX_p = currentX

for game_num in range(numGames):
    
    print(game_num)
    
    training_labels = np.array([])
    input_data = np.array([])

    for i in range(300):
        myGrid.render()
        
        # Record the true maximum action so that we can check if it has changed 
        # and if it has changed, then change the arrow in the GUI
        # original_max = np.argmax(Q_Table[currentY, currentX, :] )

        # Choose an action
        action = np.argmax(Q_value.predict( myGrid.convertToInput(currentX, currentY)  ) +  np.random.randn(1, 4) * (1.0/ ( game_num + 1.0 ) ) ) 
        
        currentY_p = currentY
        currentX_p = currentX

        # Observe the reward and the next state
        current_reward, isOver, currentX, currentY = myGrid.step(action)


        # Record the "label" 
        label = current_reward + (discount * np.amax( Q_value.predict( myGrid.convertToInput(currentX, currentY) ) ) ) 
        
        # Record the value in the training data
        # Fix me - more efficient way?
        training_labels = np.append( training_labels, label )

        # This is the input data
        input_data = np.append( input_data, myGrid.convertToInput(currentX_p, currentY_p)[0] )

        # action_final = np.argmax(Q_Table[currentY, currentX, :] )
        

        # if ( action_final != original_max ):
            # Change the arrow direction
            # changeArrow(x_grid, y_grid, direction) 
        #    myGrid.changeArrow( currentX, currentY, action_final  )


        if ( isOver == True ):
            # print("Game Over")
            myGrid.reset()
            break

    # Do a training epoch
    print(input_data)
    print(training_labels)
    print("")
    print("")
    Q_value.fit(input_data, training_labels, epochs = 10)

    
        # time.sleep(0.2)







