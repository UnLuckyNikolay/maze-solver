SCREEN_FULLSCREEN = True
# Doesn't matter if fullscreen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

    # MAZE

MAZE_X = 35
MAZE_Y = 40
MAZE_COLUMNS = 37 # 37
MAZE_ROWS = 20 # 20
MAZE_SEED_OVERRIDE = False
MAZE_SEED = 1

CELL_SIZE = 50

    # TIMERS

# Delay between restarts, in seconds, float
RESTART_DELAY = 5 # 5
# Delay between each update while drawing a maze, in seconds, float
ANIMATION_DELAY_BUILD = 0.001 # 0.001
# Delay between each update while breaking walls, in seconds, float
ANIMATION_DELAY_BREAK = 0.015 # 0.015
# Delay between each update while pathing through, in seconds, float
ANIMATION_DELAY_DRAW = 0.05 # 0.05
# Delay between each update while going backwards, in seconds, float
ANIMATION_DELAY_UNDO = 0.03 # 0.03

    # COLORS

COLOR_BACKGROUND = "gray17"
COLOR_WALL_TOP = "antiquewhite2"
COLOR_WALL_TOP_FILL = COLOR_BACKGROUND
COLOR_WALL_LIGHT = "cornsilk4"
COLOR_WALL_LIGHT_FILL = COLOR_WALL_LIGHT
COLOR_WALL_DARK = "gray10"
COLOR_WALL_DARK_FILL = COLOR_WALL_DARK
COLOR_PATH_CURRENT = "chartreuse4"
COLOR_PATH_UNDO = "brown4"

    # LINE WIDTH

WIDTH_LINE = 2
WIDTH_WALL = 4 # Keep even
HEIGHT_WALL = 5
WIDTH_CORNER = 12 # Keep even

    # DEBUG

# Puts green checkmarks over sells that has been broken in
DEBUG_CHECK_BROKEN_IN_CELL = False
DEBUG_CHECK_BROKEN_IN_COLOR = "green"
# Puts red cross over predicted dead ends
DEBUG_CHECK_DEAD_END = True
DEBUG_CHECK_DEAD_END_COLOR = "brown4"