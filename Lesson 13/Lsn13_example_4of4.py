""" lsn13_examples_4of4.py - example code from lesson 13 """
__author__ = "CS110Z"
import pythonGraph

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
    global color, place_image
    # check for click on color and change it
    if pythonGraph.mouse_button_released(pythonGraph.mouse_buttons.LEFT):
        if mouse_x < 30 and mouse_y< 29:
            color = pythonGraph.colors.BLUE
            place_image = False
        elif mouse_x < 60 and mouse_y < 29:
            color = pythonGraph.colors.YELLOW
            place_image = False
        elif mouse_x < 90 and mouse_y < 29:
            color = pythonGraph.colors.GREEN
            place_image = False
        elif mouse_x < 120 and mouse_y < 29:
            color = pythonGraph.colors.RED
            place_image = False
        elif mouse_x < 150 and mouse_y < 29:
            place_image = True  

def draw_on():
    # if the mouse is not on the pallet and the left mouse button is down do the following
    #    if an image is to be drawn draw an image at the current mouse location
    #    otherwise draw a circle at the current mouse location
    # if the mouse is not on the pallet and the left mouse button is down draw the image or the circle based
    # on global variables place_image
    if (mouse_y >= 30 or mouse_x >= 150) and pythonGraph.mouse_button_down(pythonGraph.mouse_buttons.LEFT):
        if not place_image:
            pythonGraph.draw_circle(mouse_x, mouse_y, radius, color, True)
        else:
            pythonGraph.draw_image('lander.jpg',mouse_x,mouse_y,29,29)
        if laser_on:
            pythonGraph.play_sound_effect('laser.wav')
            
def proc_keys():
    global music_on, laser_on, radius
    # if a 'c' key is pressed clear drawing window
    if pythonGraph.key_pressed('c'):
        # erase window
        pythonGraph.clear_window(pythonGraph.colors.BLACK)
    
    # if a 'p' is press key toggle play music or if music is on turn it off
    if pythonGraph.key_pressed('p'):
        if not music_on:
            pythonGraph.play_music('my_music.mp3')
        else:
            pythonGraph.stop_music()
        music_on = not music_on
        
    # if a 's' is pressed to toggle laser sound on draw - when you draw a laser sound effect
    # is played
    if pythonGraph.key_pressed('s'):
        pythonGraph.play_sound_effect('laser.wav')
        laser_on = not laser_on
        
    # if the 'escape' or 'q' key is pressed exit
    if pythonGraph.key_pressed('escape') or pythonGraph.key_pressed('q'):
        pythonGraph.close_window()
        
    # if 'up' or 'down' is pressed increase or decrese size of pen
    if pythonGraph.key_pressed('up'):
        radius += 3
    if pythonGraph.key_pressed('down') and radius >= 3:
        radius -= 3
        
# configure graphics
config()

# animiation loop
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