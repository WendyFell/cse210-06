from constants import *
from game.scripting.action import Action


class ControlShipAction(Action):

    def __init__(self, keyboard_service):
        self._keyboard_service = keyboard_service
        
    def execute(self, cast, script, callback):
        ship = cast.get_first_actor(SPACESHIP_GROUP)
        bullet = cast.get_first_actor(BULLET_GROUP)
        
        stopable = True
        if self._keyboard_service.is_key_down(LEFT): 
            ship.swing_left()
            
        elif self._keyboard_service.is_key_down(RIGHT): 
            ship.swing_right() 
            
        elif self._keyboard_service.is_key_down(SPACE):
         
            ship.fire(cast)
            stopable = False
        else: 
           ship.stop_moving()
 
                 