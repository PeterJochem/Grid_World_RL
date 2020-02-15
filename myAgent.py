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

discount = 0.5

# Search
# Describe leadIntoMove = {-1, 0, 1, 2, 3 }
def treeExpand(leadIntoMove, depth):
    
    # Store the prior state
    original_location = myGrid.current_position
    
    if ( leadIntoMove == 0):
        myGrid.moveLeft() 
    
    elif ( leadIntoMove == 1) :
        myGrid.moveRight()
    
    elif (leadIntoMove == 2):
        myGrid.moveUp()
    
    elif (leadIntoMove == 3)
        myGrid.moveDown()
    

                                      # Change to myGrid.currentY, myGrid.currentX
    left = (discount**depth) * Q_Table[currentY, currentX, 0] 

    right = (discount**depth) * Q_Table[currentY, currentX, 1] 

    up =  (discount**depth) * Q_Table[currentY, currentX, 2] 

    down = (discount**depth) * Q_Table[currentY, currentX, 3]
    
    # Undo the move
    # Double check the order on this
    myGrid.undoMove(currentY, currentX)
 
    # Return the max score - not the max index 
    max_value = 0
    if (left == right == up == down):
        max_value = random.randint(0, 3)
    else:
        # Returns the max VALUE in an array
        max_value = np.amax([left, right, up, down])
        
    # This is a reward value - not a move
    return max_value
 

# Describe here
def chooseAction(currentX, currentY):
    
    # Move left
    left_current = Q_Table[currentY, currentX, 0] + treeExpand(0, 1)

    # right = Q_Table[currentY, currentX, 1] + (discount * treeExpand() )
    right =  Q_Table[currentY, currentX, 1] + treeExpand(1, 1)

    up =  Q_Table[currentY, currentX, 1] + treeExpand(2, 1) 

    down =  Q_Table[currentY, currentX, 1] + treeExpand(3, 1)


    index_max = 0
    if (left == right == up == down):
        index_max = random.randint(0, 3)
    else:
        index_max = np.argmax([left, right, up, down])
    
    # This indicates which direction to move in
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

    
    time.sleep(0.2)


while(1):
    myGrid.render()
    pass






