import pythonGraph

# setup 
pythonGraph.open_window(700,700)
x = 350
y = 350
DELTA = 10
color = pythonGraph.colors.BLUE

while pythonGraph.window_not_closed():
    
    # erase
    pythonGraph.clear_window(pythonGraph.colors.WHITE)
    
    # if arrow keys are pressed and held down move the circle
    if pythonGraph.key_down('up'):
        y -= DELTA
    if pythonGraph.key_down('down'):
        y += DELTA
    if pythonGraph.key_down('left'):
        x -= DELTA
    if pythonGraph.key_down('right'):
        x += DELTA
    
    # draw a circle at the given corrodinates
    pythonGraph.draw_circle(x, y, 20, color, True)

    # if the 'q' key is pressed quit the program
    if pythonGraph.key_pressed('q'):
        pythonGraph.close_window()
        
    # if the 'c' key is pressed change the color of the circle to a random color
    if pythonGraph.key_pressed('c'):
        color = pythonGraph.create_random_color()
    
    # update window
    pythonGraph.update_window()