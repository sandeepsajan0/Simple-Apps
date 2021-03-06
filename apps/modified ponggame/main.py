from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

#backgroundcolour = [1, 15, 50]
from kivy.core.window import Window
Window.clearcolor = (0, 1, 0, 1)
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
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    player3 = ObjectProperty(None)
    player4 = ObjectProperty(None)
    
    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        self.ball.move()

        # bounce of paddles
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
        self.player3.bounce_ball(self.ball)
        self.player4.bounce_ball(self.ball)
        
        # bounce ball off bottom or top
        if (self.ball.y < self.y) or (self.ball.top > self.top) :
            self.ball.velocity_y *= -1

        # went of to a side to score point?
        if self.ball.x < self.x:
            self.player2.score += 1
            self.serve_ball(vel=(4, 2))
        if self.ball.x > self.width:
            self.player1.score += 1
            if self.player1.score >= 4:
                self.serve_ball(vel=(-4, 3))
            else:    
            	self.serve_ball(vel=(-2, 3))
        '''if self.player1.score >5 or self.player2.score > 5:
        	
        	self.exit()'''
        
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        

class PongApp(App):
    def build(self):
        self.load_kv("pong2.kv")
	
        game = PongGame()
        game.serve_ball()
 
        Clock.schedule_interval(game.update, -2.0 / 50.0)
        return (game)


if __name__ == '__main__':
		
    PongApp().run()
