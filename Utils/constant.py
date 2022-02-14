# Set variable for Screen
WINDOWWIDTH = 600
WINDOWHEIGHT = 768
WHD_2 = (WINDOWHEIGHT - 168) / 2
BG_X_POS = 0
BG_Y_POS = 0

# Set FPS for game
FPS = 60

# Set Parameter for Bird
BIRDWIDTH = 60
BIRDHEIGHT = 40
G = 0.5
SPEEDFLY = -9
BIRD_INDEX = 1
DEFAULT_BIRD_POS = 360
BIRD_MOVING_RANGE = 5

# Set prameter for columns
COLUMNWIDTH = 80
COLUMNHEIGHT = 500
BLANK = 200
DISTANCE = 300
COLUMNSPEED = 3
DELAY_PLAYING = 1000

# Set parameter for Arrow
ARROW_WIDTH = 60
ARROW_HEIGHT = 50
ARROW_X_POS = 170
ARROW_Y_POS = 355

# Set parameter for Logo
LOGO_WIDTH = 380
LOGO_HEIGHT = 80
LOGO_X_POS = (WINDOWWIDTH - LOGO_WIDTH)/2
LOGO_Y_POS = 100

# Set parameter for Moving_SCREEN
M_SCREEN_WIDTH = 600
M_SCREEN_HEIGHT = 180
M_SCREEN_X_POS = 0
M_SCREEN_Y_POS = 600

# Set parameter for MEDAL
MEDAL_WIDTH = 70
MEDAL_HEIGHT = 70
MEDAL_X_POS = 190
MEDAL_Y_POS = 280

# Set parameter for ScoreBoard
WT = 260
HT = 160
p1 = (WHD_2 - WT / 2, WHD_2 - HT / 2 + 10)
p2 = (WHD_2 - WT / 2 + 3, WHD_2 - HT / 2 + 3)
p3 = (WHD_2 - WT / 2 + 10, WHD_2 - HT / 2)
p4 = (WHD_2 + WT / 2 - 10, WHD_2 - HT / 2)
p5 = (WHD_2 + WT / 2 - 3, WHD_2 - HT / 2 + 3)
p6 = (WHD_2 + WT / 2, WHD_2 - HT / 2 + 10)
p7 = (WHD_2 + WT / 2, WHD_2 + HT / 2 - 10)
p8 = (WHD_2 + WT / 2 - 3, WHD_2 + HT / 2 - 3)
p9 = (WHD_2 + WT / 2 - 10, WHD_2 + HT / 2)
p10 = (WHD_2 - WT / 2 + 10, WHD_2 + HT / 2)
p11 = (WHD_2 - WT / 2 + 3, WHD_2 + HT / 2 - 3)
p12 = (WHD_2 - WT / 2, WHD_2 + HT / 2 - 10)
table = (p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)

# Set parameter for font
CHARACTER_SELECT_SIZE = 40
GAMEOVER_FONT_SIZE = 60
SYSFONT = 'arial'
SYSFONT_SIZE = 20
GUIDEFONT_SIZE = 15
SCORE_TITLE_FONT_SIZE = 20
SCORE_FONT_SIZE = 40
SCORE_FONT_SIZE_PLAYING = 50
SCORE_Y_POS_PLAYING = 100
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

# Path for Images
BACKGROUND_URL = 'Sources/images/background1.png'
MOVING_BG_URL = 'Sources/images/floor.png'
YELLOWBIRD_MID_URL = 'Sources/images/yellowbird-midflap.png'
YELLOWBIRD_UP_URL = 'Sources/images/yellowbird-upflap.png'
YELLOWBIRD_DOWN_URL = 'Sources/images/yellowbird-downflap.png'
BROWNBIRD_MID_URL = 'Sources/images/brownbird-midflap.png'
BROWNBIRD_UP_URL = 'Sources/images/brownbird-upflap.png'
BROWNBIRD_DOWN_URL = 'Sources/images/brownbird-downflap.png'
BLUEBIRD_MID_URL = 'Sources/images/bluebird-midflap.png'
BLUEBIRD_UP_URL = 'Sources/images/bluebird-upflap.png'
BLUEBIRD_DOWN_URL = 'Sources/images/bluebird-downflap.png'
COLUMN_URL = 'Sources/images/column.png'
ARROW_URL = 'Sources/images/arrow1.png'
LOGO_URL = 'Sources/images/logo.png'
GAMEOVER_LOGO_URL = 'Sources/images/gameover.png'
BRONZE_MEDAL_URL = 'Sources/images/bronze.png'
SILVER_MEDAL_URL = 'Sources/images/silver.png'
GOLD_MEDAL_URL = 'Sources/images/gold.png'
DIAMOND_MEDAL_URL = 'Sources/images/diamond.png'

# Path for Fonts
CHARACTER_SELECT_FONT_URL = 'Sources/fonts/PhoenixGaming.ttf'
GUIDEFONT_URL = 'Sources/fonts/AtariClassic.ttf'
SCORE_TITLE_FONT_URL = 'Sources/fonts/Pixel.ttf'
SCORE_FONT_URL = 'Sources/fonts/04B_19.ttf'

# Path for Sounds
CHOICE_SOUND_URL = 'Sources/sounds/menu-select.mp3'
FLAP_SOUND_URL = 'Sources/sounds/swing.wav'
HIT_SOUND_URL = 'Sources/sounds/hit.wav'
POINT_SOUND_URL = 'Sources/sounds/point.wav'
BACKGROUND_SOUND_URL = 'Sources/sounds/devastates.mp3'
BATTLE_SOUND_URL = 'Sources/sounds/Journey.mp3'
DIE_SOUND_URL = 'Sources/sounds/lushlife-gameover.wav'