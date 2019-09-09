import pythonGraph

# Global Variables
ball_x = 300
ball_y = 300
ball_x_velocity = 3
ball_y_velocity = 5

# Functions Go Here
def erase_everything():
    pythonGraph.clear_window(pythonGraph.colors.WHITE)

def draw_ball():
    pythonGraph.draw_circle(ball_x, ball_y, 10, pythonGraph.colors.BLUE, True)

def move_ball():
    global ball_x, ball_y, ball_x_velocity, ball_y_velocity
    ball_x = ball_x + ball_x_velocity
    ball_y = ball_y + ball_y_velocity
    
    if ball_x > 600 or ball_x < 0:
        ball_x_velocity = ball_x_velocity * -1
    
    if ball_y > 600 or ball_y < 0:
        ball_y_velocity = ball_y_velocity * -1

# This Opens the Graph Window
pythonGraph.open_window(600, 600)

# This is our animation loop
while pythonGraph.window_not_closed():
    # Step 1: Erase Everything on the Screen
    erase_everything()
    
    # Step 2: Move the Ball
    move_ball()
    
    # Step 3: Draw the Ball
    draw_ball()
        
    # Step 4: Update the Screen 
    pythonGraph.update_window()