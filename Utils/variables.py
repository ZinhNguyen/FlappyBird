import pygame
from Utils import constant as const
from Utils import function as fn


# Display Screen
SCREEN = pygame.display.set_mode((const.WINDOWWIDTH, const.WINDOWHEIGHT))

# Set Fps Clock
fpsClock = pygame.time.Clock()

# Load yellow bird
BIRD_MID = fn.load_scale_image(const.YELLOWBIRD_MID_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BIRD_DOWN = fn.load_scale_image(const.YELLOWBIRD_DOWN_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BIRD_UP = fn.load_scale_image(const.YELLOWBIRD_UP_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BIRD_LIST = [BIRD_DOWN, BIRD_MID, BIRD_UP]
BIRD = BIRD_LIST[const.BIRD_INDEX]

#Load blue bird
BLUEBIRD_MID = fn.load_scale_image(const.BLUEBIRD_MID_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BLUEBIRD_DOWN = fn.load_scale_image(const.BLUEBIRD_DOWN_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BLUEBIRD_UP = fn.load_scale_image(const.BLUEBIRD_UP_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BLUEBIRD_LIST = [BLUEBIRD_DOWN, BLUEBIRD_MID, BLUEBIRD_UP]
BLUEBIRD = BLUEBIRD_LIST[const.BIRD_INDEX]

#Load brown bird
BROWNBIRD_MID = fn.load_scale_image(const.BROWNBIRD_MID_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BROWNBIRD_DOWN = fn.load_scale_image(const.BROWNBIRD_DOWN_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BROWNBIRD_UP = fn.load_scale_image(const.BROWNBIRD_UP_URL, const.BIRDWIDTH, const.BIRDHEIGHT)
BROWNBIRD_LIST = [BROWNBIRD_DOWN, BROWNBIRD_MID, BROWNBIRD_UP]
BROWNBIRD = BROWNBIRD_LIST[const.BIRD_INDEX]

BIRD_INDEX = const.BIRD_INDEX
BIRD_FLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRD_FLAP, 50)

MEDAL_WIDTH = const.MEDAL_WIDTH
MEDAL_HEIGHT = const.MEDAL_HEIGHT
# Load bronze medal images
BRONZE_MEDAL = fn.load_scale_image(const.BRONZE_MEDAL_URL, MEDAL_WIDTH, MEDAL_HEIGHT)

# Load silver medal images
SILVER_MEDAL = fn.load_scale_image(const.SILVER_MEDAL_URL, MEDAL_WIDTH, MEDAL_HEIGHT)

# Load gold medal images
GOLD_MEDAL = fn.load_scale_image(const.GOLD_MEDAL_URL, MEDAL_WIDTH, MEDAL_HEIGHT)

# Load diamond medal images
DIAMOND_MEDAL = fn.load_scale_image(const.DIAMOND_MEDAL_URL, MEDAL_WIDTH, MEDAL_HEIGHT)