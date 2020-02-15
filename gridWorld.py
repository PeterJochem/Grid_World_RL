import numpy as np
from graphics import *
import random

class grid:

    # Constructor
    def __init__(self, length, width, currentX, currentY, goalX, goalY):
        
        self.startX = currentX
        self.startY = currentY

        self.current_position = np.array([currentY, currentX])
                
        # Grid dimensions
        self.length = length
        self.width = width
            
        # Window dimensions
        self.window_width = 8 * 100
        self.window_length = 8 * 100

        self.goalX = goalX
        self.goalY = goalY
    
        self.states = np.zeros( (length, width) )
        self.rewards = np.zeros( (length, width) )
        # This is really just for testing
        self.setRewards()

        self.isOver = False
    
        # Create a window for us to display the game's state
        self.window = GraphWin("Grid_World", self.window_length , self.window_width)
        self.window.setBackground("white")
            
        self.render_setup()


    def reset(self):
         # Put it into a random location??????
         newStartY = random.randint(0, self.length - 1)
         newStartX = random.randint(0, self.width - 1)
         self.current_position = np.array([newStartY, newStartX])
         self.isOver = False

    
    # Describe here 
    def setRewards(self):
        
        # distance to reward
        # Going out of bounds
        pass     




    def moveLeft(self):
        
        if ( self.current_position[1] == 0):
            self.isOver = True
        else:
            self.current_position[1] = self.current_position[1] - 1

    def undo_Move(self, priorLocations):
        priorX = priorLocations[1]
        priorY = priorLocations[0]
        
        # Move the agent back to its prior location
        self.current_position[0] = priorY
        self.current_position[1] = priorX


    def moveRight(self):

        if ( self.current_position[1] == (self.width - 1) ):
            self.isOver = True
        else:
            self.current_position[1] = self.current_position[1] + 1
    
    def moveDown(self):
        
        if ( self.current_position[0] == (self.length - 1) ):
            self.isOver = True
        else:
            self.current_position[0] =  self.current_position[0] + 1
        

    def moveUp(self):

        if ( self.current_position[0] == 0 ):
            self.isOver = True
        else:
            self.current_position[0] = self.current_position[0] - 1

    # This method will display the grid world
    def render_setup(self):

        self.rectangles = []
        
        # Store the list of points needed to draw the board
        points = [] 
        
        for i in range( self.length):
            
            current_row_rectangles = []
                
            Point_1 = Point( 0 , 0 ) 
            for j in range( self.width ):
                
                current_row = float(self.window_width) / float(self.width)
                current_column =  float(self.window_length) / float(self.length) 

                Point_1 = Point( current_row * j , current_column * i )  
                Point_2 = Point( current_row * (j + 1) , current_column * (i + 1) )
                
                current_row_rectangles.append( Rectangle(Point_1, Point_2) )


            # Append the next row to the array
            self.rectangles.append(current_row_rectangles)

        # Traverse the list of the rectangles to change their fill colors
        if ( self.window != None ):
            for i in  range( len( self.rectangles  ) ):
                for j in range( len( self.rectangles[i] ) ):
                    
                    self.rectangles[i][j].draw(self.window)
                    
                    if( (i == self.current_position[0] ) and (j == self.current_position[1] ) ):
                         self.rectangles[i][j].setFill("blue")

                    elif( (i == self.goalY) and (j == self.goalX) ):
                         self.rectangles[i][j].setFill("green")
                    else:
                        self.rectangles[i][j].setFill("white")
       
                    

                    # Set the current state's color

                    # Set the current state's goal state's color 
    
    def render(self):
        
        # Traverse the list of the rectangles to change their fill colors
        if ( self.window != None ):
            for i in  range( len( self.rectangles  ) ):
                for j in range( len( self.rectangles[i] ) ):


                    if( (i == self.current_position[0] ) and (j == self.current_position[1] ) ):
                         self.rectangles[i][j].setFill("blue")

                    elif( (i == self.goalY) and (j == self.goalX) ):
                         self.rectangles[i][j].setFill("green")
                    else:
                        self.rectangles[i][j].setFill("white")


    # Take the system from the current state 
    # to the state after doing the given action
    # Input: 
    # Return: reward, isOver 
    def step(self, action):
       
        if ( action == 0 ):
            self.moveLeft()
        
        elif (action == 1 ):
            self.moveRight()
        
        elif ( action == 2 ):
            self.moveUp()
        
        elif( action == 3 ):
            self.moveDown()

        # Compute the given reward function
        reward = 0
        if ( ( (self.goalY == self.current_position[0] ) and (self.goalX == self.current_position[1] ) ) ):
            reward = 100
            print("Game Won")
            self.isOver = True


        return reward, self.isOver, self.current_position[1], self.current_position[0]
    




