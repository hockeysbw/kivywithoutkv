from kivy.properties import NumericProperty
from kivy.graphics import Rectangle

from kivy.uix.widget import Widget

from graphic_widget import GraphicWidget
from pong_ball import PongBall
from pong_paddle import PongPaddle


class PongGame(GraphicWidget):

    GraphicClass = Rectangle
    color_tuple = (0.2, 0.2, 0.2, 1)

    def __init__(self):
        super(PongGame, self).__init__()
         self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
         self._keyboard.bind(on_key_down=self._on_keyboard_down)

          def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        print keycode
        return True



        # make a ball
        self.ball = PongBall()
        # add it to the stage
        self.add_widget(self.ball)

        self.balltwo = PongBall()
        self.balltwo.x = 50
        self.balltwo.y = 50
        self.add_widget(self.balltwo)

        self.player1 = PongPaddle()
        self.add_widget(self.player1)

        self.player2 = PongPaddle()
        self.player2.x = 790
        self.add_widget(self.player2)

    def serve_ball(self):


        self.ball.center = self.center
        self.ball.velocity_x = -3
        self.ball.velocity_y = 4

        self.balltwo.center = self.center
        self.balltwo.velocity_x = 3
        self.balltwo.velocity_y = -4

    def update(self, dt):
        for b in [ self.ball, self.balltwo ] :

            b.move()

            # bounce of paddles
            self.player1.bounce_ball(b)
            self.player2.bounce_ball(b)

            # bounce ball off bottom or top
            if b.top > self.top:
                b.velocity_y = random
            elif b.y < self.y:
                b.velocity_y = random


            # went of to a side to score point?
            if b.x < self.x:
                self.player2.score += 1
                self.serve_ball()
            if b.x > self.width:
                self.player1.score += 1
                self.serve_ball()

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y



#speeds up again because did not chage throughout the whole thing. Not sure how to make it
#so it remains.
