SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MAZE_X = 35
MAZE_Y = 40
MAZE_COLUMNS = 37 # 14
MAZE_ROWS = 20 # 10
MAZE_SEED_OVERRIDE = False
MAZE_SEED = 1

    # TIMERS

# Delay between restarts, in seconds, float
RESTART_DELAY = 5
# Delay between each update while drawing a maze, in seconds, float
ANIMATION_DELAY_BUILD = 0.005
# Delay between each update while breaking walls, in seconds, float
ANIMATION_DELAY_BREAK = 0.03
# Delay between each update while pathing through, in seconds, float
ANIMATION_DELAY_DRAW = 0.05
# Delay between each update while going backwards, in seconds, float
ANIMATION_DELAY_UNDO = 0.03

    # COLORS

COLOR_BACKGROUND = "gray10"
COLOR_WALL = "antiquewhite2"
COLOR_PATH_CURRENT = "chartreuse4"
COLOR_PATH_UNDO = "brown4"

COLOR_CHECK = "green"

WIDTH_LINE = 2
WIDTH_WALL = 4
WIDTH_CORNER = 10


# Puts green checkmarks over sells that has been broken in
CHECK_BROKEN_IN_CELL = False