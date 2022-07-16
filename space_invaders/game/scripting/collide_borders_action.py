from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action

class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        

    def execute(self, cast, script, callback):
        aliens = cast.get_actors(ALIENS_GROUP)
        
        
        
        for alien in aliens:
                
            
            alien_body = alien.get_body()
            position = alien_body.get_position()
            x = position.get_x()
            y = position.get_y()

        if y >= (FIELD_BOTTOM - ALIENS_WIDTH):
        
            callback.on_next(GAME_OVER)
            
