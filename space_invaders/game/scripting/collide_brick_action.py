from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBrickAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BULLET_GROUP)
        bricks = cast.get_actors(ALIENS_GROUP)
        stats = cast.get_first_actor(STATS_GROUP)
        racket = cast.get_first_actor(SPACESHIP_GROUP)
        
        for brick in bricks:
            ball_body = ball.get_body()
            brick_body = brick.get_body()

            if self._physics_service.has_collided(ball_body, brick_body):
                
                sound = Sound(SHOOTING_SOUND)
                self._audio_service.play_sound(sound)
                points = brick.get_points()
                stats.add_points(points)
                
                ball.new_bullet(racket._body.get_position())
                
                cast.remove_actor(ALIENS_GROUP, brick)