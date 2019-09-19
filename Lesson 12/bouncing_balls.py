import pythonGraph, math

# Ball Radius
BALL_RADIUS = 10

# Global Variables
ball_1_x = 300
ball_1_y = 300
ball_1_x_velocity = 3
ball_1_y_velocity = 5

ball_2_x = 400
ball_2_y = 400
ball_2_x_velocity = -3
ball_2_y_velocity = -5

# Functions Go Here
def dist_points(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

def erase_everything():
    pythonGraph.clear_window(pythonGraph.colors.WHITE)

def draw_ball():
    pythonGraph.draw_circle(ball_1_x, ball_1_y, BALL_RADIUS, pythonGraph.colors.BLUE, True)
    pythonGraph.draw_circle(ball_2_x, ball_2_y, BALL_RADIUS, pythonGraph.colors.RED, True)

def move_ball():
    global ball_1_x, ball_1_y, ball_1_x_velocity, ball_1_y_velocity
    ball_1_x = ball_1_x + ball_1_x_velocity
    ball_1_y = ball_1_y + ball_1_y_velocity
    
    if ball_1_x > 600 or ball_1_x < 0:
        ball_1_x_velocity = ball_1_x_velocity * -1
    
    if ball_1_y > 600 or ball_1_y < 0:
        ball_1_y_velocity = ball_1_y_velocity * -1
    
    global ball_2_x, ball_2_y, ball_2_x_velocity, ball_2_y_velocity
    ball_2_x = ball_2_x + ball_2_x_velocity
    ball_2_y = ball_2_y + ball_2_y_velocity
    
    if ball_2_x > 600 or ball_2_x < 0:
        ball_2_x_velocity = ball_2_x_velocity * -1
    
    if ball_2_y > 600 or ball_2_y < 0:
        ball_2_y_velocity = ball_2_y_velocity * -1
    
    distance = dist_points(ball_1_x, ball_1_y, ball_2_x, ball_2_y)
    if distance <= 2 * BALL_RADIUS:
        ball_1_x_velocity = ball_1_x_velocity * -1
        ball_1_y_velocity = ball_1_y_velocity * -1
        ball_2_x_velocity = ball_2_x_velocity * -1
        ball_2_y_velocity = ball_2_y_velocity * -1

# This Opens the Graph Window
pythonGraph.open_window(600, 600)

# This is our animation loop
while pythonGraph.window_not_closed():
    # Step 1: Erase Everything on the Screen
    #erase_everything()
    
    # Step 2: Move the Ball
    move_ball()
    
    # Step 3: Draw the Ball
    draw_ball()
        
    # Step 4: Update the Screen 
    pythonGraph.update_window()
