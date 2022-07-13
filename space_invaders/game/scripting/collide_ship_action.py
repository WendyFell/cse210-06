from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


# class CollideShipAction(Action):

#     def __init__(self, physics_service, audio_service):
#         self._physics_service = physics_service
#         self._audio_service = audio_service
        
#     def execute(self, cast, script, callback):
#         #bullet = cast.get_first_actor(BULLET_GROUP)
#         ship = cast.get_first_actor(SPACESHIP_GROUP)
        
#         #bullet_body = bullet.get_body()
#         ship_body = ship.get_body()

#         # if self._physics_service.has_collided(bullet_body, ship_body):
#         #     bullet.bounce_y()
                