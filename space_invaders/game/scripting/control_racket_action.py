from constants import *
from game.scripting.action import Action


class ControlRacketAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(SPACESHIP_GROUP)
        bullet = cast.get_first_actor(BULLET_GROUP)
        
        stopable = True
        if self._keyboard_service.is_key_down(LEFT): 
            racket.swing_left()
        #    bullet.swing_left()
            
        elif self._keyboard_service.is_key_down(RIGHT): 
            racket.swing_right() 
         #   bullet.swing_right() 
            
        elif self._keyboard_service.is_key_down(SPACE):
            print(1)
            racket._add_ball(cast)
            racket.fire(cast)
            #bullet = cast.get_first_actor(BULLET_GROUP)  
            # bullet.release()
            # bullet.new_bullet()
            stopable = False
        else: 
            racket.stop_moving()
            #if stopable:
               # bullet.stop_moving()  
                 