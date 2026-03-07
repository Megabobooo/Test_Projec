"""module that handles classes and functions for the main loop of the programm"""
import pyglet
import random
from pyglet import shapes
import logic

random.seed()


class Button():
    def __init__(self,x,y,x2,y2,batch,image_when_pressed,image_when_not_pressed):
        self.button  = pyglet.gui.PushButton(x,y,batch=batch,pressed=image_when_pressed,unpressed=image_when_not_pressed)
        self.second_x = x2
        self.second_y = y2

class Programm_Init():
    def init_window(window_one_width=900,window_one_height=900,window_one_text="aaa",visibility = True):
        """initialises one window"""
        window = pyglet.window.Window(window_one_width,window_one_height,window_one_text)
        window.set_visible(visibility)
        return window
    def init_batch():
        """initialises a batch"""
        return pyglet.graphics.Batch() 
    def init_button(x,y,x2,y2,batch,image_when_pressed,image_when_not_pressed):
        """initialises button"""
        button = Button(x,y,x2,y2,batch,image_when_pressed,image_when_not_pressed)
        return button
    def main_window_deco(batch):
        """handels decoratve elements on the main window"""
        a,b,c = assets.create_penis(100,100,batch=batch)
        return a,b,c
    def setup_window_deco(batch):
        """handels decoratve elements on the setup window"""
        d,e,f = assets.create_penis(100,100,batch=batch) 
        arc = shapes.Arc(500,500,10, color=(0, 255, 0), thickness=3,batch=batch)
        return d,e,f,arc
    
    def game_window_deco(batch):
        """handels decoratve elements on the game window"""
        curve = logic.TerrainGenerator.create_bezier_curve(batch=batch)
        return curve
    def text_entry(batch):
        label = pyglet.text.Label(text="",x=100,y=200,width=100,height=100,batch=batch)
        return label
    
class assets():
    def create_penis(x,y,batch):
        ball_left = shapes.Arc(x,y, 10, color=(0, 255, 0), thickness=3,batch=batch)
        ball_right = shapes.Arc(x+20,y, 10, color=(0, 255, 0), thickness=3,batch=batch)
        main_part = shapes.Rectangle(x,y,20,200,color=(0, 255, 0),batch=batch)
        return ball_left,ball_right,main_part
    
