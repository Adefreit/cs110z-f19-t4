import pythonGraph
import random

# This variable is our LOOP CONTROL VARIABLE.
# It determines how many times the loop iterates (and by extension, how many lines are drawn)
num_lines = 10

# Here, we are opening the pythonGraph window
pythonGraph.open_window(600, 600)

# In this loop, we generate a random set of x,y coordinates for the line, and draw them
for i in range(num_lines):
    x1 = random.randint(0, 600)
    y1 = random.randint(0, 600)
    x2 = random.randint(0, 600)
    y2 = random.randint(0, 600)
    
    pythonGraph.draw_line(x1, y1, x2, y2, pythonGraph.create_random_color(), 3)

# We wait for the window to close
pythonGraph.wait_for_close()