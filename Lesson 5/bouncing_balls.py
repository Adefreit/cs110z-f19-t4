import pythonGraph
import random

SCREEN_TITLE = "Bouncing Balls (the PINNACLE of Computer Science 110)"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Gets the number of balls from the user
ball_x = []
ball_y = []
ball_x_velocity = []
ball_y_velocity = []
ball_radius = []
ball_color = []

# Setup tasks for window
pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
pythonGraph.set_window_title(SCREEN_TITLE)

# Animation Loop
while pythonGraph.window_not_closed():
    pythonGraph.clear_window(pythonGraph.colors.WHITE)
    
    for i in range(0, len(ball_x)):
        pythonGraph.draw_circle(ball_x[i], ball_y[i], ball_radius[i], ball_color[i], True)
        
        ball_x[i] += ball_x_velocity[i]
        ball_y[i] += ball_y_velocity[i]
        
        if ball_x[i] < 0 or ball_x[i] > SCREEN_WIDTH:
            ball_x_velocity[i] *= -1
        if ball_y [i] < 0 or ball_y[i] > SCREEN_HEIGHT:
            ball_y_velocity[i] *= -1    

    if pythonGraph.mouse_button_pressed(pythonGraph.mouse_buttons.LEFT):
        ball_x.append(pythonGraph.get_mouse_x())
        ball_y.append(pythonGraph.get_mouse_y())
        ball_x_velocity.append(random.randint(1,10))
        ball_y_velocity.append(random.randint(1,10))
        ball_radius.append(random.randint(10,30))
        ball_color.append(pythonGraph.create_random_color())
        print("clicked")

    pythonGraph.update_window()
