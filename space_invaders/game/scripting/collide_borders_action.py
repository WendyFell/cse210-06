from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action
from game.casting.point import Point


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        try:
            pass
            # racket = cast.get_first_actor(SPACESHIP_GROUP)
            # ball = cast.get_first_actor(BULLET_GROUP)
            # body = ball.get_body()
            # position = body.get_position()
            # x = position.get_x()
            # y = position.get_y()
            # if self._physics_service.has_collided(Point(0,y), Point(0,FIELD_TOP)):
            #     cast.remove_actor(BULLET_GROUP, ball)
            #     cast.add_actor(BULLET_GROUP, ball._body.set_position(racket._body.get_position))
            
            #bounce_sound = Sound(SHOOTING_SOUND)
            # over_sound = Sound(OVER_SOUND)
                    
            #if x < FIELD_LEFT:
            #     ball.bounce_x()
            #     self._audio_service.play_sound(bounce_sound)

            # elif x >= (FIELD_RIGHT - BULLET_WIDTH):
            #     ball.bounce_x()
            #     self._audio_service.play_sound(bounce_sound)

            #if y < FIELD_TOP:
            #    cast.remove_actor(BULLET_GROUP, ball)
                #cast.add_actor(BULLET_GROUP, ball._body.set_position(racket._body.get_position))
            #     self._audio_service.play_sound(bounce_sound)

            # elif y >= (FIELD_BOTTOM - BULLET_WIDTH):
            #     stats = cast.get_first_actor(STATS_GROUP)
            #     stats.lose_life()
                
            #     if stats.get_lives() > 0:
            #         callback.on_next(TRY_AGAIN) 
            #     else:
            #         callback.on_next(GAME_OVER)
            #         self._audio_service.play_sound(over_sound)
        except:
            pass