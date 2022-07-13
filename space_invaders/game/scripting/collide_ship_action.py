from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideShipAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        
        aliens = cast.get_actors(ALIENS_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        ship = cast.get_first_actor(SPACESHIP_GROUP)
        try:
            for alien in aliens:
                
                ship_body = ship.get_body()
                alien_body = alien.get_body()

                if self._physics_service.has_collided(ship_body, alien_body):
                    
                    #sound = Sound(SHOOTING_SOUND)
                    #self._audio_service.play_sound(sound)
                    #points = alien.get_points()
                    #stats.add_points(points)
                    
                    stats = cast.get_first_actor(STATS_GROUP)
                    stats.lose_life()
                    
                    if stats.get_lives() > 0:
                        callback.on_next(TRY_AGAIN) 
                    else:
                        callback.on_next(GAME_OVER)
                        self._audio_service.play_sound(OVER_SOUND)
        except:
            pass
                