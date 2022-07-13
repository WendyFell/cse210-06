from secrets import choice
from constants import *
from game.scripting.action import Action
from game.casting.point import Point
from game.casting.bullet import Bullet


class MoveAlienAction(Action):

    def __init__(self):
        self.x = 1
        
    def execute(self, cast, script, callback):
        aliens = cast.get_actors(ALIENS_GROUP)
        level = cast.get_actors(LEVEL_GROUP)
        
        if self.x % 10 == 0:
            for alien in aliens:
                
                body = alien.get_body()
                #if level == 1:
                velocity = Point(0,10)
                position = body.get_position()
                position = position.add(velocity)
                body.set_position(position)
        self.x += 1
        