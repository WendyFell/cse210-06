from constants import *
from game.scripting.action import Action
from game.casting.point import Point


class MoveAlienAction(Action):

    def __init__(self):
        self.x = 1
        
    def execute(self, cast, script, callback):
        aliens = cast.get_actors(ALIENS_GROUP)
        level = cast.get_first_actor(STATS_GROUP)
        levels = level.get_level()
        
        if self.x % 10 == 0:
            for alien in aliens:
                
                body = alien.get_body()
                if levels == 1:
                    velocity = Point(0, 1)
                    position = body.get_position()
                    position = position.add(velocity)
                    body.set_position(position)
                    
                if levels == 2:
                    velocity = Point(0, 1.5)
                    position = body.get_position()
                    position = position.add(velocity)
                    body.set_position(position) 
                    
                if levels == 3:
                    velocity = Point(0, 2)
                    position = body.get_position()
                    position = position.add(velocity)
                    body.set_position(position)           
                    
                    
        self.x += 1
        