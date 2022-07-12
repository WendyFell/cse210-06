from constants import *
from game.casting.actor import Actor


class BG(Actor):
    """Adds a background for the game"""
    
    def __init__(self, body, animation, points, debug = False):
        """Constructs a new BG.
        
        Args:
            body: A new instance of Body.
            image: A new instance of Image.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._points = points
        
    def get_animation(self):
        """Gets the aliens's image.
        
        Returns:
            An instance of Image.
        """
        return self._animation

    def get_body(self):
        """Gets the aliens's body.
        
        Returns:
            An instance of Body.
        """
        return self._body