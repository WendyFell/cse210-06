from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class MoveAlienAction(Action):

    def __init__(self):
        self.x = 1
        
    def execute(self, cast, script, callback):
        aliens = cast.get_actors(ALIENS_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        level = stats.get_level()
        if level == 1: 
            time = 100
        else:
            time = 110 - (level * 15)
        if time < 10:
            time = 10
        if self.x % time == 0:
            for alien in aliens:
                body = alien.get_body()
                velocity = Point(0,10)
                position = body.get_position()
                position = position.add(velocity)
                body.set_position(position)
        self.x += 1
        