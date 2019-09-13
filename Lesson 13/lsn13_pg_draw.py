""" lsn13_examples_4of4.py - example code from lesson 13 """
__author__ = "CS110Z"
import pythonGraph

""" Instructions:  Find the TODO sections below and complete after skimming through the
    entire file.  The TODO's are numbered.  Start with TODO #1.
"""

# global variables
radius = 6  #radius of pen (circle used for drawing)
color = pythonGraph.colors.BLUE # set the initial color
place_image = False # do we draw a circle or an image
music_on = False # music is initially off
laser_on = False # laser sound is initially off

def config():
    # setup
    pythonGraph.open_window(700,700)
    pythonGraph.clear_window(pythonGraph.colors.BLACK)
    pythonGraph.set_window_title('PythonGraph Draw')

def draw_pallet():
    # draw color / image pallet
    pythonGraph.draw_rectangle(0,0,29,29, pythonGraph.colors.BLUE, True)
    pythonGraph.draw_rectangle(30,0,59,29, pythonGraph.colors.YELLOW, True)
    pythonGraph.draw_rectangle(60,0,89,29, pythonGraph.colors.GREEN, True)
    pythonGraph.draw_rectangle(90,0,119,29, pythonGraph.colors.RED, True)
    pythonGraph.draw_image('lander.jpg',120,0,29,29)
    
def pallet_click():
    """ TODO #2: Complete and test the pallet_click function. Functionality is
        described in the comments below.  Test prior to continuing.
    """
    global color, place_image
    # check for click on color and change it (first color is done for you)
    if pythonGraph.mouse_button_released(pythonGraph.mouse_buttons.LEFT):
        if mouse_x < 30 and mouse_y< 29:
            color = pythonGraph.colors.BLUE
            place_image = False  

def draw_on():
    """ TODO #1: Complete and test the draw_on function. Functionality is
        described in the comments below.  Test prior to continuing.
    """
    if pythonGraph.mouse_button_down(pythonGraph.mouse_buttons.LEFT):
        if place_image == True:
            pythonGraph.draw_image('lander.jpg', mouse_x, mouse_y, 29, 29)
        else:
            pythonGraph.draw_circle(mouse_x, mouse_y, 10, color, True)

            
def proc_keys():
    """ TODO #3: Complete and test the proc_keys function. Functionality is
        described in the comments below.  Test prior to continuing.
    """
    global music_on, laser_on, radius
    # if a 'c' key is pressed clear drawing window
   
    
    # if a 'p' is press key toggle play music or if music is on turn it off
   
        
    # if a 's' is pressed to toggle laser sound on draw - when you draw a laser sound effect
    # is played
    
        
    # if the 'escape' or 'q' key is pressed exit
    
        
    # if 'up' or 'down' is pressed increase or decrese size of pen
    pass  # placeholder no-op remove this
   
        
# configure graphics window
config()

# animiation loop (no modifications required)
while pythonGraph.window_not_closed():

    # draw the pallet
    draw_pallet()
    
    # get the coordinates of the mouse
    mouse_x = pythonGraph.get_mouse_x()
    mouse_y = pythonGraph.get_mouse_y()

    # draw circle or image on the canvas
    draw_on()

    # handle all key presses
    proc_keys()
    
    # check for click on color and change it
    pallet_click()
    
    # update window
    pythonGraph.update_window()