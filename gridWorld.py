import numpy as np
from graphics import *

class grid:

    # Constructor
    def __init__(self, length, width, goalX, goalY):
        
        self.current_position = np.array([ 0, 0])
        self.length = length
        self.width = width
        self.goalX = goalX
        self.goalY = goalY
        self.states = np.zeros( (length, width) ) 
        self.isOver = False
    
        # Create a window for us to display the game's state
        self.window = GraphWin("Grid_World", self.length * 100, self.width * 100)


    def moveLeft(self):
        
        if ( self.current_position[1] == 0):
            self.isOver = True
        
    def moveRight(self):

        if ( self.current_position[1] == (self.width - 1) ):
            self.isOver = True

    def moveDown(self):
        
        if ( self.current_position[0] == (self.length - 1) ):
            self.isOver = True

    def moveUp(self):

        if ( self.current_position[0] == 0 ):
            self.isOver = True

    # This method will display the grid world
    def render(self):
        # print("")
        # print(self.states)
        # print("")
            
        self.window.setBackground("black")
        


    # Take the system from the current state 
    # to the state after doing the given action
    # Input: 
    # Output: reward, 
    def step(self, action):
        
        if ( action == 0 ):
            self.moveLeft()
        
        elif (action == 1 ):
            self.moveRight()
        
        elif ( action == 2 ):
            self.moveUp()
        
        elif( action == 3 ):
            self.moveDown()

        # Check for the end of the game  
        if ( self.isOver == True ):
            # return, what to do here?
            pass 
    




