"""module that handles classes and functions for the main loop of the programm"""
import pyglet
import random
from pyglet import shapes

random.seed()


class Programm_Init():
    def init_window(window_one_width=1200,window_one_height=1200,widow_one_text="aaa"):
        """initialises one window"""
        window = pyglet.window.Window(window_one_width,window_one_height,widow_one_text)
        return window
    def init_batch():
        """initialises a batch"""
        return pyglet.graphics.Batch() 

class assets():
    def create_penis(x,y,batch):
        ball_left = shapes.Arc(x,y, 10, color=(0, 255, 0), thickness=3,batch=batch)
        ball_right = shapes.Arc(x+20,y, 10, color=(0, 255, 0), thickness=3,batch=batch)
        main_part = shapes.Rectangle(x,y,20,200,color=(0, 255, 0),batch=batch)
        return ball_left,ball_right,main_part