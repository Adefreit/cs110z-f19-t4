""" lsn13_examples_1of4.py - example code from lesson 13 """
__author__ = "CS110Z"
import pythonGraph

# setup 
pythonGraph.open_window(700,700)
erase_on = True

while pythonGraph.window_not_closed():
    
    # erase if erase is on
    if erase_on:
        pythonGraph.clear_window(pythonGraph.colors.WHITE)
    
    # get the coordinates of the mouse
    mouse_x = pythonGraph.get_mouse_x()
    mouse_y = pythonGraph.get_mouse_y()

    # draw a circle at the current coordinates of the mouse
    pythonGraph.draw_circle(mouse_x, mouse_y, 10, pythonGraph.colors.BLUE, True)

    # if the left mouse button is held down draw a circle at the location and
    # don't erase the screen
    if pythonGraph.mouse_button_down(pythonGraph.mouse_buttons.LEFT):
        erase_on = False
        #pythonGraph.draw_circle(mouse_x, mouse_y, 10, pythonGraph.colors.BLUE, True)
    
    # if the mouse button is released turn erase on
    if pythonGraph.mouse_button_released(pythonGraph.mouse_buttons.LEFT):
        erase_on = True

    # update window
    pythonGraph.update_window()