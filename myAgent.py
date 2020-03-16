import numpy as np
import gridWorld
import graphics 
import time
import random
import tensorflow as tf
from tensorflow import keras

# Create our grid
length = 6
width =  6

goalX = length / 2
goalY = width / 2

currentX = 1
currentY = 1

# Create object to hold all the information associated with the grid
myGrid = gridWorld.grid(length, width, currentX, currentY, goalX, goalY)

discount = 0.80
learning_rate = 0.80

numGames = 100000

# Define the neural network structure
Q_value = keras.Sequential([
    keras.layers.Dense(30, input_dim = length * width ),
    keras.layers.Dense(20),
    keras.layers.Dense(10),
    keras.layers.Dense(4)
])


# Set more of the model's parameters
optimizer = tf.keras.optimizers.RMSprop(0.0005)

Q_value.compile(loss='mse',
                optimizer=optimizer,
                metrics=['mae', 'mse'])

# This defines how much data to generate before training
batch_size = 40

# These will hold the in/out data pairs
training_labels = []
input_data = []

# This defines the explore rate
epsilon = 0.5
# This defines the rate at which epsilon (ie the explore rate) will decay
epsilonDecay = 0.9

# Prior state tracking
currentY_p = currentY
currentX_p = currentX

for game_num in range(1, numGames):
    
    for i in range(20):
        myGrid.render(Q_value)
        
        # Choose an action
        # 0 - 4 is left, right, up, down
        # argmax returns the index of the max element
        action = np.argmax( Q_value.predict( myGrid.convertToInput(currentX, currentY) ) )
            
        # Explore or not?
        if ( epsilon > random.random() ):
            # Choose action randomnly
            action = random.randrange(4)
            
        # Track the prior location
        currentY_p = currentY
        currentX_p = currentX

        # Observe the reward and the next state
        current_reward, isOver, currentX, currentY = myGrid.step(action)

        # Record the "label" 
        label = Q_value.predict( myGrid.convertToInput(currentX, currentY) )
        
        # Compute the bellman equation
        label[0][action] = current_reward + (discount * np.amax( Q_value.predict( myGrid.convertToInput(currentX, currentY) ) ) ) 
       
        # Format the data for Tensorflow
        label = np.array( label[0] )
        training_labels.append(label)

        # This is the input data
        input_data.append(  myGrid.convertToInput(currentX_p, currentY_p)[0] )
        
        if ( isOver == True ):
            myGrid.reset()
            break
    
    # Do a training epoch 
    if (game_num % batch_size == 0):
        
        # Format the data for Tensorflow
        input_data = np.array(input_data)
        training_labels = np.array(training_labels)
       
        # Update the Q-Table
        Q_value.fit(input_data, training_labels, epochs = 12)

        # Traverse the grid and redraw the arrows
        for i in range(myGrid.length):
            for j in range (myGrid.width):
            
                # 0 - 4 is left, right, up, down
                action = Q_value.predict( myGrid.convertToInput(j, i) ) 

                action = np.argmax(action)
 
                # Re-draw arrow  
                myGrid.changeArrow(j, i, action)
        
        # Let the epsilon rate decay - i.e. explore less
        epsilon = epsilon * epsilonDecay

        training_labels = []
        input_data = [] 







