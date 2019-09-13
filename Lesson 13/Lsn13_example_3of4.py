""" lsn13_examples_3of4.py - example code from lesson 13 """
__author__ = "CS110Z"
import pythonGraph, random

# setup 
pythonGraph.open_window(700,700)

while pythonGraph.window_not_closed():
     
    # draw a circle at the random corrodinates
    pythonGraph.draw_circle(random.randint(0,699), random.randint(0,699), random.randint(10,70), pythonGraph.create_random_color(), True)
      
    # if the 's' key is pressed stop the music
    if pythonGraph.key_pressed('s'):
        pythonGraph.stop_music()
    
    # if 'p' key is pressed play some background music
    if pythonGraph.key_pressed('p'):
        pythonGraph.play_music('my_music.mp3')
    
    # if the left mouse button is pressed play a sound effect and clear the screen
    if pythonGraph.mouse_button_released(pythonGraph.mouse_buttons.LEFT):
        pythonGraph.play_sound_effect('laser.wav')
        pythonGraph.clear_window(pythonGraph.colors.WHITE)
    
    # update window
    pythonGraph.update_window()
