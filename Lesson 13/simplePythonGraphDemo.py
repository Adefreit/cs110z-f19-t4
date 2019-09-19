import pythonGraph

pythonGraph.open_window(600, 600)

while pythonGraph.window_not_closed():
           
    if (pythonGraph.mouse_button_down(pythonGraph.mouse_buttons.LEFT)):
        mouse_x = pythonGraph.get_mouse_x()
        mouse_y = pythonGraph.get_mouse_y()
        pythonGraph.draw_circle(mouse_x, mouse_y, 10, pythonGraph.colors.BLUE, True)
    
    pythonGraph.update_window()