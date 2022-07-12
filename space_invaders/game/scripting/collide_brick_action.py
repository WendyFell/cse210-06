from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        bullet = cast.get_first_actor(BULLET_GROUP)
        aliens = cast.get_actors(ALIENS_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        ship = cast.get_first_actor(SPACESHIP_GROUP)
        try:
            for alien in aliens:
                
                bullet_body = bullet.get_body()
                alien_body = alien.get_body()

                if self._physics_service.has_collided(bullet_body, alien_body):
                    
                    sound = Sound(SHOOTING_SOUND)
                    self._audio_service.play_sound(sound)
                    points = alien.get_points()
                    stats.add_points(points)
                    
                    cast.remove_actor(ALIENS_GROUP, alien)
                    cast.remove_actor(BULLET_GROUP, bullet)
                    cast.add_actor(BULLET_GROUP, bullet._body.set_position(ship._body.get_position))
        except:
            pass