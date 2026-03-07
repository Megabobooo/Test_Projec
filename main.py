"""handles the core of the programm"""
import pyglet
import random
from pyglet import shapes
import manage_programm
import collisions
import logic

def main():
    """main body of the game"""
    picture = pyglet.image.load('assets/button_start_asset.png')
    picture2 = pyglet.image.load('assets/start_game_button.png')

    main_window = manage_programm.Programm_Init.init_window(window_one_text="Main_Window")
    main_batch = manage_programm.Programm_Init.init_batch()
    main_button = manage_programm.Programm_Init.init_button(500,500,700,550,batch=main_batch,image_when_not_pressed=picture,image_when_pressed=picture)
    main_deco = manage_programm.Programm_Init.main_window_deco(main_batch)

    setup_window = manage_programm.Programm_Init.init_window(window_one_text="setup_window",visibility=False)
    setup_batch = manage_programm.Programm_Init.init_batch()
    setup_button = manage_programm.Programm_Init.init_button(500,700,700,750,batch=setup_batch,image_when_not_pressed=picture2,image_when_pressed=picture2)
    setup_deco = manage_programm.Programm_Init.setup_window_deco(setup_batch)
    setup_text_field = manage_programm.Programm_Init.text_entry(setup_batch)

    game_window = manage_programm.Programm_Init.init_window(window_one_text="game_window",visibility=False)
    game_batch = manage_programm.Programm_Init.init_batch()
    game_deco = manage_programm.Programm_Init.game_window_deco(game_batch)
    
    @main_window.event
    def on_draw():
        main_window.switch_to()
        main_window.clear()
        main_batch.draw()

    @main_window.event
    def on_mouse_press(x,y,button,modifiers):
        if collisions.Mouse_collisions.button_pressed(main_button,x,y):
            setup_window.set_visible(True)
            main_window.close()

    @main_window.event
    def on_close():
        setup_window.close()
        game_window.close()

    @setup_window.event 
    def on_draw():
        setup_window.switch_to()
        setup_window.clear()
        setup_batch.draw()

    @setup_window.event
    def on_key_press(symbol,modifiers):
        logic.TerrainGenerator.text_field_logic(setup_text_field,symbol)

    @setup_window.event
    def on_mouse_press(x,y,button,modifiers):
        if collisions.Mouse_collisions.button_pressed(setup_button,x,y):
            game_window.set_visible(True)
            setup_window.close()

    @setup_window.event()
    def on_close():
        game_window.close()
    
    @game_window.event 
    def on_draw():
        game_window.switch_to()
        game_window.clear()
        game_batch.draw()
        

    pyglet.app.run()

if __name__ == "__main__":
    main()