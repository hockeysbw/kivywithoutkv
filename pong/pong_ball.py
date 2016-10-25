from kivy.graphics import Ellipse
from kivy.properties import NumericProperty
from kivy.vector import Vector

from graphic_widget import GraphicWidget


class PongBall(GraphicWidget):

    GraphicClass = Ellipse

    # For Ellipse
    width = NumericProperty(100)
    height = NumericProperty(100)
    x = NumericProperty(0)
    y = NumericProperty(0)

    #             R   G   B   A
    color_tuple = (.16, .93, .77, 1)

    # Stuff we made
    velocity_x = 0
    velocity_y = 0

    def move(self):
        new_x = self.x + self.velocity_x
        new_y = self.y + self.velocity_y
        self.pos = (new_x, new_y)
