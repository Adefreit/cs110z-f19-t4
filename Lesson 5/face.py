import pythonGraph

SCREEN_TITLE = "Python Graph Demonstration"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Setup tasks for window
pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
pythonGraph.set_window_title(SCREEN_TITLE)

# DRAWING goes here
pythonGraph.draw_circle(290, 250, 100, pythonGraph.colors.YELLOW, True)
pythonGraph.draw_circle(250, 200, 20, pythonGraph.colors.BLACK, True)
pythonGraph.draw_circle(330, 200, 20, pythonGraph.colors.BLACK, True)
pythonGraph.draw_line(230, 300, 350, 300, pythonGraph.colors.BLACK)

# Wait using the window is closed
pythonGraph.wait_for_close()

