import numpy as np
from graphics import *
import random


# This class describes the graphics objects needed to draw an arrow
# Each cell in the grid will have a corresponding arrow object
class arrow:

    # (x, y) is the location in the grid
    # width and length are the number of cells in the grid
    # window_width and window_length are the pixel dimensions of the grid 
    def __init__(self, x, y, width, length, window_width, window_length, window):
            
        self.window = window
        
        self.color = "blue"
        self.width = 2

        # This descirbes which direction the arrow is currently pointing
        # 0 = left
        # 1 = right
        # 2 = up
        # 3 = down
        self.currentDirection = 0

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
        self.Point_5 = Point( self.Point_1.x - (delta_y), self.Point_2.y - (0.10 * ( float(window_width) / float(width)  ) ) )  
        self.Point_6 = Point( self.Point_1.x + (delta_y), self.Point_2.y - (0.10 * ( float(window_width) / float(width)  ) ) )
        
        # These points define the down arrow's hat
        self.Point_7 = Point( self.Point_2.x - (delta_y), self.Point_1.y + (0.10 * ( float(window_width) / float(width)  ) ) )
        self.Point_8 = Point( self.Point_2.x + (delta_y), self.Point_1.y + (0.10 * ( float(window_width) / float(width)  ) ) )

        delta_y = (0.10 * ( float(window_length) / float(length) ) )
        # These points define the left arrow's hat
        self.Point_9 = Point( self.Point_3.x + (delta_y), self.Point_3.y - (0.05 * ( float(window_width) / float(width)  ) ) )
        self.Point_10 = Point( self.Point_3.x + (delta_y), self.Point_3.y + (0.05 * ( float(window_width) / float(width)  ) ) )
        
        # These points define the right arrow's hat
        self.Point_11 = Point( self.Point_4.x - (delta_y), self.Point_4.y - (0.05 * ( float(window_width) / float(width)  ) ) )
        self.Point_12 = Point( self.Point_4.x - (delta_y), self.Point_4.y + (0.05 * ( float(window_width) / float(width)  ) ) )
        
        
        # Define all the lines we need for each grid
        # Each arrow has three lines - the principal axis and two lines that make the "hat"
        # These lines define the up arrow
        self.line_1 = Line(self.Point_1, self.Point_2)
        self.line_1.setFill(self.color)
        self.line_1.setWidth(self.width)

        self.line_2 = Line(self.Point_5, self.Point_2)
        self.line_2.setFill(self.color)
        self.line_2.setWidth(self.width)

        self.line_3 = Line(self.Point_6, self.Point_2)
        self.line_3.setFill(self.color)
        self.line_3.setWidth(self.width)


        # These lines define the down arrows
        self.line_4 = Line(self.Point_1, self.Point_2)
        self.line_4.setFill(self.color)
        self.line_4.setWidth(self.width) 


        self.line_5 = Line(self.Point_7, self.Point_1)
        self.line_5.setFill(self.color)
        self.line_5.setWidth(self.width)

        self.line_6 = Line(self.Point_8, self.Point_1)
        self.line_6.setFill(self.color)
        self.line_6.setWidth(self.width)

        
        # These lines define the left arrow
        self.line_7 = Line(self.Point_3, self.Point_4)
        self.line_7.setFill(self.color)
        self.line_7.setWidth(self.width)


        self.line_8 = Line(self.Point_9, self.Point_3)
        self.line_8.setFill(self.color)
        self.line_8.setWidth(self.width)


        self.line_9 = Line(self.Point_10, self.Point_3)
        self.line_9.setFill(self.color)
        self.line_9.setWidth(self.width)
    

        # These lines define the left arrow
        self.line_10 = Line(self.Point_3, self.Point_4)
        self.line_10.setFill(self.color)
        self.line_10.setWidth(self.width)


        self.line_11 = Line(self.Point_11, self.Point_4)
        self.line_11.setFill(self.color)
        self.line_11.setWidth(self.width)

        self.line_12 = Line(self.Point_12, self.Point_4)
        self.line_12.setFill(self.color)
        self.line_12.setWidth(self.width)
 

    # This draws the down arrow
    def draw_down_arrow(self):
        
        self.remove_arrow()
        
        self.currentDirection = 3

        self.line_1.draw(self.window)

        self.line_2.draw(self.window)

        self.line_3.draw(self.window)

    # This draws the up arrow
    def draw_up_arrow(self):

        self.remove_arrow()

        self.currentDirection = 2

        self.line_4.draw(self.window)

        self.line_5.draw(self.window)

        self.line_6.draw(self.window)

    # This draws the left arrow
    def draw_left_arrow(self):
        
        self.remove_arrow()

        self.currentDirection = 0

        self.line_7.draw(self.window)

        self.line_8.draw(self.window)

        self.line_9.draw(self.window) 

    # This draws the right arrow 
    def draw_right_arrow(self):

        self.remove_arrow()
            
        self.currentDirection = 1
        
        self.line_10.draw(self.window)

        self.line_11.draw(self.window)

        self.line_12.draw(self.window)
    
    # This method undraws the current arrow at the given location
    def remove_arrow(self):
        
        # 0 - 4 is left, right, up, down
        
        if (self.currentDirection == 0):
            self.line_7.undraw()

            self.line_8.undraw()

            self.line_9.undraw()

        elif (  self.currentDirection == 1 ):
                
            self.line_10.undraw()

            self.line_11.undraw()
         
            self.line_12.undraw()


        elif(  self.currentDirection == 2  ):
            self.line_4.undraw()

            self.line_5.undraw()
    
            self.line_6.undraw()

        elif ( self.currentDirection == 3 ):
            self.line_1.undraw()

            self.line_2.undraw()

            self.line_3.undraw()
    


# This class holds all the information related to the graphic grid
class grid:

    # length and width are the number of cells in the grid
    # currentX and currentY are the agent's initial location
    # goalX and goalY are the agent's desired location
    def __init__(self, length, width, currentX, currentY, goalX, goalY):
        
        self.startX = currentX
        self.startY = currentY
    
        # The agent's current position
        self.current_position = np.array([currentY, currentX])
                
        # Grid dimensions
        self.length = length
        self.width = width
            
        # Window dimensions
        self.window_width = 8 * 100
        self.window_length = 8 * 100

        # Create a list of arrow objects
        # This will hold graphics objects 
        self.arrows = []
        
        # Records the agent's goal state
        self.goalX = goalX
        self.goalY = goalY
        
        # Create data structure to record the grid's shape
        self.states = np.zeros( (length, width) )
        
        # This records if the game is over or not
        self.isOver = False
    
        # Create a window for us to display the game's state
        self.window = GraphWin("Grid_World", self.window_length, self.window_width)
        self.window.setBackground("white")
           
        # Create the graphic's objects needed to draw board
        self.render_setup()

        
    # This method converts the agent's x, y location into the format 
    # needed for the neural network
    def convertToInput(self, current_X, current_Y):
        
        myArray = np.zeros( 36, )
        
        myArray[current_Y * self.width + current_X] = 1.0

        return np.array( [ myArray ] )
        # return myArray    
        # return np.array( [current_Y * self.width + current_X] )


    # This method resets the agent to a random initial start state 
    def reset(self):
         newStartY = random.randint(0, self.length - 1)
         newStartX = random.randint(0, self.width - 1)
         self.current_position = np.array([newStartY, newStartX])
         self.isOver = False
    
    # This method change's the arrow at the grid (x,y) 
    def changeArrow(self, x_grid, y_grid, direction):
        
        # Don't draw the arrow on the goal state
        if ( (x_grid == self.goalX ) and (y_grid == self.goalY) ):
            return

        # 0 - 4 is left, right, up, down
        if ( direction == 0 ):
            self.arrows[y_grid][x_grid].draw_left_arrow()
        elif ( direction == 1):
             self.arrows[y_grid][x_grid].draw_right_arrow()
        elif ( direction == 2 ):
             self.arrows[y_grid][x_grid].draw_up_arrow()
        elif ( direction == 3 ):
             self.arrows[y_grid][x_grid].draw_down_arrow()


    # This moves the agent one grid to the left
    def moveLeft(self):
        
        if ( self.current_position[1] == 0):
            self.isOver = True
        else:
            self.current_position[1] = self.current_position[1] - 1
        
    # This method undoes the prior move
    def undo_Move(self, priorLocations):
        priorX = priorLocations[1]
        priorY = priorLocations[0]
        
        # Move the agent back to its prior location
        self.current_position[0] = priorY
        self.current_position[1] = priorX

    # Move the agent right one square
    def moveRight(self):

        if ( self.current_position[1] == (self.width - 1) ):
            self.isOver = True
        else:
            self.current_position[1] = self.current_position[1] + 1
    
    # Move the agent down one square
    def moveDown(self):
        
        if ( self.current_position[0] == (self.length - 1) ):
            self.isOver = True
        else:
            self.current_position[0] =  self.current_position[0] + 1
        
    # Move the agent up one square
    def moveUp(self):

        if ( self.current_position[0] == 0 ):
            self.isOver = True
        else:
            self.current_position[0] = self.current_position[0] - 1
    

    # Draw an up arrow at the given location (x, y)
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


    # This method will create the graphics objects needed for the grid world
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
                    
                    # Draw the rectangle
                    self.rectangles[i][j].draw(self.window)
                    
                    # Set the rectangle's color
                    if( (i == self.current_position[0] ) and (j == self.current_position[1] ) ):
                         self.rectangles[i][j].setFill("blue")

                    elif( (i == self.goalY) and (j == self.goalX) ):
                         self.rectangles[i][j].setFill("green")
                    
                    else:
                        self.rectangles[i][j].setFill("white")
                    
                    self.rectangles[i][j].setWidth("4")
                    
                    # Don't draw an arrow on the goal state
                    if ( (i == self.goalY ) and (j == self.goalX) ):
                        continue

                    # Set the arrow's initial directions
                    direction = random.random()
                    
                    # Draw random arrows to represent the initial policy
                    if ( direction < 0.25):
                        self.arrows[i][j].draw_up_arrow()
                    elif( (direction > 0.25) and (direction < 0.50) ):
                        self.arrows[i][j].draw_down_arrow()
                    elif ( (direction > 0.50) and (direction < 0.75)  ):
                        self.arrows[i][j].draw_left_arrow()
                    elif( (direction > 0.75) ):
                        self.arrows[i][j].draw_right_arrow()


    # This method will draw the board
    def render(self, Q_value):
        
        # Traverse the list of the rectangles to change their fill colors
        if ( self.window != None ):
            for i in  range( len( self.rectangles  ) ):
                for j in range( len( self.rectangles[i] ) ):

                    if( (i == self.current_position[0] ) and (j == self.current_position[1] ) ):
                         self.rectangles[i][j].setFill("blue")

                    elif( (i == self.goalY) and (j == self.goalX) ):
                         self.rectangles[i][j].setFill("green")
                    else:
                        # customColor = color_rgb(128, 0, 255)
                        #current_value = np.amax( Q_value.predict( self.convertToInput(j, i) ) )
                        #colorValue = int(current_value * 200)
                        #if (colorValue > 255):
                        #    colorValue = 254
                        #if ( colorValue < 0):
                        #    colorValue = 0
                        #self.rectangles[i][j].setFill( color_rgb(0, 0, colorValue ) )
                        self.rectangles[i][j].setFill( "white" )
        



    # Take the system from the current state 
    # to the state after doing the given action
    # Input: the action to take
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
        reward = -1
        if ( ( (self.goalY == self.current_position[0] ) and (self.goalX == self.current_position[1] ) ) ):
            
            reward = 1
            # print("Game Won")
            self.isOver = True


        return reward, self.isOver, self.current_position[1], self.current_position[0]
    




