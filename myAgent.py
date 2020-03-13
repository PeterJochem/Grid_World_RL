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
length = 2
width =  3
goalX = 0
goalY = 1
currentX = 0
currentY = 0
myGrid = gridWorld.grid(length, width, currentX, currentY, goalX, goalY)

discount = 0.99
learning_rate = 0.80
epsilonDecay = 0.95

numGames = 100000

# Create the neural network
Q_value = keras.Sequential([
    keras.layers.Dense(10, input_shape = (1, ) ),
    keras.layers.Dense(10),
    keras.layers.Dense(4)
])

# Set more of the model's parameters
optimizer = tf.keras.optimizers.RMSprop(0.001)

Q_value.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])


batch_size = 30
# use np.append()
# training_labels = np.array([])
training_labels = []
input_data = []
# input_data = np.array([])

# Get some batch of data to train on and then call the lie below
# model.fit(train_images, train_labels, epochs=10)

epsilon = 0.2

# Prior state tracking
currentY_p = currentY
currentX_p = currentX

for game_num in range(1, numGames):
    
    print(game_num)
    
    # training_labels = np.array([])
    # input_data = np.array([])

    for i in range(20):
        myGrid.render()
        
        # Record the true maximum action so that we can check if it has changed 
        # and if it has changed, then change the arrow in the GUI
        # original_max = np.argmax(Q_Table[currentY, currentX, :] )

        # Choose an action
        # 0 - 4 is left, right, up, down
        #print(myGrid.convertToInput(currentX, currentY) )
        action1 = Q_value.predict( myGrid.convertToInput(currentX, currentY) ) # +  np.random.randn(1, 1) * (1.0/ ( game_num + 1.0 ) ) 
        #action2 = Q_value.predict( myGrid.convertToInput(currentX + 1, currentY) ) # +  np.random.randn(1, 1) * (1.0/ ( game_num + 1.0 ) )
        #action3 = Q_value.predict( myGrid.convertToInput(currentX, currentY + 1) ) # +  np.random.randn(1, 1) * (1.0/ ( game_num + 1.0 ) )
        #action4 = Q_value.predict( myGrid.convertToInput(currentX, currentY - 1) ) # +  np.random.randn(1, 1) * (1.0/ ( game_num + 1.0 ) )  
        
        # This returns index 
        action = np.argmax( [action1 ] )

        if ( epsilon > random.random() ):
            # Choose axtion randomnly
            action = random.randrange(4)
            
        # print([action1, action2, action3, action4] )

        # action = np.argmax(Q_value.predict( myGrid.convertToInput(currentX, currentY)  ) )
        

        currentY_p = currentY
        currentX_p = currentX

        # Observe the reward and the next state
        current_reward, isOver, currentX, currentY = myGrid.step(action)

        # Record the "label" 
        label = Q_value.predict( myGrid.convertToInput(currentX, currentY) )
        # print(label)
        label[0][action] = current_reward + (discount * np.amax( Q_value.predict( myGrid.convertToInput(currentX, currentY) ) ) ) 
        

        # Record the value in the training data
        # Fix me - more efficient way?
        
        label =  np.array([ label[0][0], label[0][1], label[0][2], label[0][3] ] ) 
        training_labels.append(label)
        # training_labels = np.insert( training_labels, label, axis = 1)

        # This is the input data
        input_data.append(  myGrid.convertToInput(currentX_p, currentY_p) )

        #print("The input data is " + str(input_data) )
        #print("The label is " + str(training_labels) )

        # action_final = np.argmax(Q_Table[currentY, currentX, :] )
        

        # if ( action_final != original_max ):
            # Change the arrow direction
            # changeArrow(x_grid, y_grid, direction) 
        #    myGrid.changeArrow( currentX, currentY, action_final  )


        if ( isOver == True ):
            # print("Game Over")
            myGrid.reset()
            break
    
    
    if ( game_num % batch_size == 0 ):
        # Do a training epoch
        # print(input_data)
        # print(training_labels)
        # print("")
        # print("")
        input_data = np.array(input_data)
        training_labels = np.array(training_labels)
        Q_value.fit(input_data, training_labels, epochs = 5)
        # myGrid.drawMaxArrow()
        # Traverse the grid and redraw the arrows
        for i in range( myGrid.length):
            for j in range (myGrid.width):
                 # def changeArrow(self, x_grid, y_grid, direction)
            
                # 0 - 4 is left, right, up, down
                action = Q_value.predict( myGrid.convertToInput(j - 1, i) ) 

                action = np.argmax( action  )
 
                myGrid.changeArrow(j, i, action)

        epsilon = epsilon * epsilonDecay
        training_labels = [] #np.array([])
        input_data = [] # np.array([])







