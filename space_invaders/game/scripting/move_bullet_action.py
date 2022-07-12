from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.bullet import Bullet


class MoveBulletAction(Action):

    def __init__(self):
        pass
        
    def execute(self, cast, script, callback):
        pass
        bullet = cast.get_first_actor(BULLET_GROUP)
        if type(bullet) is Bullet:
            body = bullet.get_body()
            position = body.get_position()
            velocity = body.get_velocity()
            position = position.add(velocity)
            x = position.get_x()
            if x < 0:
                position = Point(0, position.get_y())
            elif x > (SCREEN_WIDTH - SPACESHIP_WIDTH):
                position = Point(SCREEN_WIDTH - SPACESHIP_WIDTH, position.get_y())
                
            body.set_position(position)