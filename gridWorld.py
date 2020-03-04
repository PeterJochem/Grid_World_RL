import numpy as np
from graphics import *
import random


# Describe here
class arrow:

    # Describe input parameters
    def __init__(self, x, y, width, length, window_width, window_length, window):
        
        self.window = window

        # Compute center_x and center_y of the grid
        center_x = (0.5 + x) * ( float(window_width) / float(width) )
        center_y = (0.5 + y) * ( float(window_length) / float(length) )

        # Add points for the vertical directions
        self.Point_1 = Point( center_x , center_y - (0.20 * ( float(window_length) / float(length) ) ) )
        self.Point_2 = Point( center_x , center_y + (0.20 * ( float(window_length) / float(length) ) ) )
    
        # Add points for the horizontal directions
        self.Point_3 = Point( center_x - (0.20 * ( float(window_width) / float(width)  ) ), center_y )
        self.Point_4 = Point( center_x + (0.20 * ( float(window_width) / float(width) ) ), center_y  )
        

        # Add the points that define the "hats" of the arrows
        # These are the "hats" of the vertically upwards arrow
        delta_y = (0.10 * ( float(window_width) / float(width) ) )
        self.Point_5 = Point( self.Point_1.x - (delta_y), self.Point_1.y + (0.10 * ( float(window_width) / float(width)  ) ) )  
        self.Point_6 = Point( self.Point_1.x + (delta_y), self.Point_1.y + (0.10 * ( float(window_width) / float(width)  ) ) )
        
        # These points define the down arrow's hat
        self.Point_7 = Point( self.Point_2.x - (delta_y), self.Point_2.y - (0.10 * ( float(window_width) / float(width)  ) ) )
        self.Point_8 = Point( self.Point_2.x + (delta_y), self.Point_2.y - (0.10 * ( float(window_width) / float(width)  ) ) )

        # These points define the left arrow's hat
        self.Point_9 = Point( self.Point_3.x + (delta_y), self.Point_3.y - (0.10 * ( float(window_width) / float(width)  ) ) )
        self.Point_10 = Point( self.Point_3.x + (delta_y), self.Point_3.y + (0.10 * ( float(window_width) / float(width)  ) ) )
        
        # These points define the left arrow's hat
        self.Point_11 = Point( self.Point_4.x - (delta_y), self.Point_4.y - (0.10 * ( float(window_width) / float(width)  ) ) )
        self.Point_12 = Point( self.Point_4.x - (delta_y), self.Point_4.y + (0.10 * ( float(window_width) / float(width)  ) ) )
        
        
        # Define all the lines we need for each grid
        # Each arrow has three lines - the principal axis and two lines that make the "hat"
        # These lines define the up arrow
        self.line_1 = Line(self.Point_1, self.Point_2)
        self.line_1.setFill("green")

        self.line_2 = Line(self.Point_5, self.Point_2)
        self.line_2.setFill("green")

        self.line_3 = Line(self.Point_6, self.Point_2)
        self.line_3.setFill("green")


        # These lines define the down arrows
        self.line_4 = Line(self.Point_1, self.Point_2)
        self.line_4.setFill("green")

        self.line_5 = Line(self.Point_7, self.Point_1)
        self.line_5.setFill("green")

        self.line_6 = Line(self.Point_8, self.Point_1)
        self.line_6.setFill("green")

        
        # These lines define the left arrow
        self.line_7 = Line(self.Point_3, self.Point_4)
        self.line_7.setFill("green")

        self.line_8 = Line(self.Point_9, self.Point_3)
        self.line_8.setFill("green")

        self.line_9 = Line(self.Point_10, self.Point_3)
        self.line_9.setFill("green")

        # These lines define the left arrow
        self.line_10 = Line(self.Point_3, self.Point_4)
        self.line_10.setFill("green")

        self.line_11 = Line(self.Point_11, self.Point_4)
        self.line_11.setFill("green")

        self.line_12 = Line(self.Point_12, self.Point_4)
        self.line_12.setFill("green")


    # Describe method here
    def draw_down_arrow(self):
        
        self.line_1.draw(self.window)

        self.line_2.draw(self.window)

        self.line_3.draw(self.window)

    # Describe here
    def draw_up_arrow(self):
        self.line_4.draw(self.window)

        self.line_5.draw(self.window)

        self.line_6.draw(self.window)
    
    # Describe here
    def draw_left_arrow(self):
        self.line_7.draw(self.window)

        self.line_8.draw(self.window)

        self.line_9.draw(self.window) 

    # Describe method here 
    def draw_right_arrow(self):
        self.line_10.draw(self.window)

        self.line_11.draw(self.window)

        self.line_12.draw(self.window)
   
   # remove arrow



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

        # Create a list of arrows
        self.arrows = []

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
    

    # Describe method here
    def draw_up_arrow(self, x, y):
        
        # Compute center_x and center_y of the grid
        center_x = (0.5 + x) * ( float(self.window_width) / float(self.width) ) 
        center_y = (0.5 + y) * ( float(self.window_length) / float(self.length) )  

        # Add point A
        Point_1 = Point( center_x , center_y - (0.20 * ( float(self.window_length) / float(self.length) ) ) ) 

        # Add point B
        Point_2 = Point( center_x , center_y + (0.20 * ( float(self.window_length) / float(self.length) )) )

        # Add the graphics object to a list so we can
        # modify/remove it later
        
        myLine = Line(Point_1, Point_2)
        
        #myLine.draw(self.window)
         
        #myLine.setFill("green")


    



    # This method will display the grid world
    def render_setup(self):

        self.rectangles = []
        
        # Store the list of points needed to draw the board
        points = [] 
        
        for i in range( self.length):
            
            current_row_rectangles = []
            current_row_arrows = []


            Point_1 = Point( 0 , 0 ) 
            for j in range( self.width ):
                
                current_row = float(self.window_width) / float(self.width)
                current_column =  float(self.window_length) / float(self.length) 

                Point_1 = Point( current_row * j , current_column * i )  
                Point_2 = Point( current_row * (j + 1) , current_column * (i + 1) )
                
                current_row_rectangles.append( Rectangle(Point_1, Point_2) )
                current_row_arrows.append(arrow( j, i, self.width, self.length, self.window_width, self.window_length, self.window) )
                

            # Append the next row to the array
            self.rectangles.append(current_row_rectangles)
            self.arrows.append(current_row_arrows)


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
       
                    # Testing the arrow drawing
                    self.arrows[i][j].draw_right_arrow()    

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
    




