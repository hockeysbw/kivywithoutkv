from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    ball2 = ObjectProperty(None)
    ball3 = PongBall()
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def __init__(self):
        super(PongGame, self).__init__()
        self.add_widget(self.ball3)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel
        self.ball2.center = self.center
        self.ball2.velocity = (3, 2)
        self.ball3.center = self.center
        self.ball3.velocity = (-3, 4)
        
        

    def update(self, dt):

        for b in [self.ball, self.ball2, self.ball3]:
            b.move()

            #bounce of paddles
            self.player1.bounce_ball(b)
            self.player2.bounce_ball(b)

            #bounce ball off bottom or top
            if (b.y < self.y) or (b.top > self.top):
                b.velocity_y *= -1

            #went of to a side to score point?
            if b.x < self.x:
                self.player2.score += 1
                self.serve_ball(vel=(4, 0))
            if b.x > self.width:
                self.player1.score += 1
                self.serve_ball(vel=(-4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()