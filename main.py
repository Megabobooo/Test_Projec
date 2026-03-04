"""handles the core of the programm"""
import pyglet
import random
from pyglet import shapes
import manage_programm

def main():
    """main body of the game"""
    main_window = manage_programm.Programm_Init.init_window()
    main_batch = manage_programm.Programm_Init.init_batch()
    a,b,c = manage_programm.assets.create_penis(100,100,main_batch)
    
    @main_window.event
    def on_draw():
        main_window.switch_to()
        main_window.clear()
        main_batch.draw()
    pyglet.app.run()

if __name__ == "__main__":
    main()