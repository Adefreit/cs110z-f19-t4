import pythonGraph
import random

SCREEN_TITLE = "Just a Circle (or is it . . .)"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

# Gets the number of balls from the user
ball_x = 400
ball_y = 400
ball_x_velocity = 8
ball_y_velocity = -5

# Gets the Number of Times
frame_count = 0

# Animation Flag
animate = False

# Setup tasks for window
pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
pythonGraph.set_window_title(SCREEN_TITLE)

# Animation Loop
while pythonGraph.window_not_closed():
    pythonGraph.clear_window(pythonGraph.colors.WHITE)
    
    # Draws Some Text
    pythonGraph.draw_text("# of Times Drawn: " + str(frame_count), 0, 0, pythonGraph.colors.BLACK)
    
    # Draws the Circle
    pythonGraph.draw_circle(ball_x, ball_y, 35, pythonGraph.colors.RED, True)
        
    # Toggles Animation Mode
    if pythonGraph.key_pressed('space'):
        animate = not animate
        
    if animate or pythonGraph.mouse_button_pressed(pythonGraph.mouse_buttons.LEFT):
        ball_x = ball_x + ball_x_velocity
        ball_y = ball_y + ball_y_velocity
      
        if ball_x < 0 or ball_x > SCREEN_WIDTH:
            ball_x_velocity *= -1
        if ball_y < 0 or ball_y > SCREEN_HEIGHT:
            ball_y_velocity *= -1
        
        frame_count = frame_count + 1

    pythonGraph.update_window()
