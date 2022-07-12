import random
import math
from constants import *
from game.casting.actor import Actor
from game.casting.point import Point


class Bullet(Actor):
    """A solid, spherical object that shoots the aliens."""
    
    def __init__(self, body, image, debug = False):
        """Constructs a new Bullet.

        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._image = image
        self.angle = 90

    def bounce_x(self):
        """Bounces the ball in the x direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x() * rn * -1
        vy = velocity.get_y()
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def bounce_y(self):
        """Bounces the ball in the y direction."""
        velocity = self._body.get_velocity()
        rn = random.uniform(0.9, 1.1)
        vx = velocity.get_x()
        vy = velocity.get_y() * rn * -1 
        velocity = Point(vx, vy)
        self._body.set_velocity(velocity)

    def get_body(self):
        """Gets the bullet's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def get_image(self):
        """Gets the bullet's image.
        
        Returns:
            An instance of Image.
        """
        return self._image
        
    def release(self):
        """Release the bullet in a given direction."""
        vx = math.sin(math.radians(self.angle + 90 )) * BULLET_VELOCITY    
        vy = math.cos(math.radians(self.angle + 90)) * BULLET_VELOCITY
        velocity = Point(0, vy)
        self._body.set_velocity(velocity)
        

    def new_bullet(self, ship_position):
        """Release a new bullet in a given direction."""
        self._body.set_velocity(Point(0,0))
        self._body.set_position(Point(CENTER_X, SCREEN_HEIGHT - SPACESHIP_HEIGHT))

    def swing_left(self):
        """Steers the bullet to the left."""
        velocity = Point(-SPACESHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the bullet to the right."""
        velocity = Point(SPACESHIP_VELOCITY, 0)
        self._body.set_velocity(velocity)

    def stop_moving(self):
        """Stops the bullet from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)    



   