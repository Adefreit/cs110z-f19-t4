import pythonGraph

def draw_a_face(x, y):
    # This is the main circle
    pythonGraph.draw_circle(x, y, 50, pythonGraph.colors.YELLOW, True)
    
    # Left Eye
    pythonGraph.draw_circle(x-25, y-25, 5, pythonGraph.colors.BLACK, True)
    
    # Right Eye
    pythonGraph.draw_circle(x+25, y-25, 5, pythonGraph.colors.BLACK, True)
    
    # Mouth
    pythonGraph.draw_line(x-25, y+25, x+25, y+25, pythonGraph.colors.BLACK, 3)
    
    
    
    
    
    