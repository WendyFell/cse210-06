from game.casting.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# GAME
GAME_NAME = "Space Invaders"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 900
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "space_invaders/assets/fonts/zorque.otf"
FONT_SMALL = 32
FONT_LARGE = 48

# BACKGROUND
BG_GROUP = 'bg'
BG_FILE = "space_invaders/assets/images/303.png"
BG_WIDTH = 1040
BG_HEIGHT = 640

# SOUND
SHOOTING_SOUND = "space_invaders/assets/sounds/shooting.wav"
WELCOME_SOUND = "space_invaders/assets/sounds/intro.wav"
OVER_SOUND = "space_invaders/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
LEFT = "left"
RIGHT = "right"
SPACE = "space" #Shoots
ENTER = "enter"
PAUSE = "p"

# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4

# LEVELS
LEVEL_FILE = "space_invaders/assets/data/level-{:03}.txt"
BASE_LEVELS = 3

# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP = "stats"
DEFAULT_LIVES = 1
MAXIMUM_LIVES = 5

# HUD
HUD_MARGIN = 15
LEVEL_GROUP = "level"
LIVES_GROUP = "lives"
SCORE_GROUP = "score"
LEVEL_FORMAT = "LEVEL: {}"
LIVES_FORMAT = "LIVES: {}"
SCORE_FORMAT = "SCORE: {}"

# BULLET
BULLET_GROUP = "bullets"
BULLET_IMAGE = "space_invaders/assets/images/000.png"
BULLET_WIDTH = 28
BULLET_HEIGHT = 28
BULLET_VELOCITY = 15

# SPACESHIP
SPACESHIP_GROUP = "spaceship"
SPACESHIP_IMAGES = [f"space_invaders/assets/images/120.png"]
SPACESHIP_WIDTH = 80
SPACESHIP_HEIGHT = 80
SPACESHIP_RATE = 6
SPACESHIP_VELOCITY = 7

# ALIENS
ALIENS_GROUP = "aliens"
ALIENS_IMAGES = {
    "b": [f"space_invaders/assets/images/011.png"],
    "g": [f"space_invaders/assets/images/020.png"],
    "w": [f"space_invaders/assets/images/030.png"],
    "y": [f"space_invaders/assets/images/012.png"], #pink
    "u": [f"space_invaders/assets/images/031.png"], #purple
    "z": [f"space_invaders/assets/images/041.png"]  #white
}
ALIENS_WIDTH = 40
ALIENS_HEIGHT = 40
ALIENS_DELAY = 0.5
ALIENS_RATE = 4
ALIENS_POINTS = 50

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER"