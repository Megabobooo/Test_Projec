"""module that handles classes and functions that have to do with internal logic"""
import pyglet
import random
from pyglet import shapes

random.seed()

class TerrainGenerator():
    def generate_points():
        """generates set of points for a bezier curve"""
        set = []
        for i in range(random.randrange(5,15)):
            set.append((random.randrange(1,1200),random.randrange(1,1200)))
        set.append(set[0])
        return set
    def semi_random_points():
        """create points of a bezier curve so that it oops but doesnt intersect itself"""
        new_set = []
        set = [
            (100,400),(300,500),(100,800),(400,1100),(800,1100),(500,800),(1100,800),(700,500),(1100,400),(800,100),(500,300),(400,100)
        ]
        for element in set:
            x,y = element
            x += random.randrange(-300,300)
            y += random.randrange(-300,300)
            new_set.append((x,y))
        new_set.append(new_set[0])
        return new_set
    
    def create_bezier_curve(batch):
        """returns random bezier curve"""
        curve = shapes.BezierCurve(*TerrainGenerator.semi_random_points(),color=(255,0,0),batch=batch)
        return curve
    
    def text_field_logic(textfield,symbol):
        """"text feld logik dings da bumgs da"""
        if symbol == 65288:
                textfield.text = textfield.text[:-1]
        if len(textfield.text) < 15:
            if 97 <= symbol <= 122:
                textfield.text += chr(symbol)
            elif symbol == 32:
                textfield.text += " "