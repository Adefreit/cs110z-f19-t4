import pythonGraph

SCREEN_TITLE = "Python Graph Demonstration"
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Setup tasks for window
pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
pythonGraph.set_window_title(SCREEN_TITLE)

# DRAWING goes here
pythonGraph.write_text("Welcome to PythonGraph!", 5, 5, pythonGraph.colors.BLACK)

# Wait using the window is closed
pythonGraph.wait_for_close()
