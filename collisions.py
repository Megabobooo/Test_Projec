"""module that handles classes and functions for collisions"""
import pyglet
import random
from pyglet import shapes
import manage_programm

random.seed()

class Mouse_collisions():
    def button_pressed(button:manage_programm.Button,mouse_x,mouse_y):
        """in an onpress event(orr similar) checks if mouse is on button"""
        if mouse_x>button.button.x and mouse_x<button.second_x and mouse_y>button.button.y and mouse_y<button.second_y:
            return True
        else:
            return False