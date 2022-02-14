import pygame, sys
from pygame.locals import *
from Image import content as ct, scoreBoard as sc, logo as lg
from Sound import gameover as so
from Utils import constant as const, variables as var, function as fn

def Gameover(bird, columns, score, record, mscreen, background):
    """
    This function will display Loading Screen

    Parameters:
        bird (object): The bird will be displayed in Screen
        columns (object): The Column will be displayed
        score (object): The Score will be displayed
        record (int) : The number will be displayed
        mscreen (object): The moving screen at the bottom will be displayed
        background (object): The background will be displayed

    Returns:
        no return
    """
    goGuide = ct.Content(const.GUIDEFONT_URL, const.GUIDEFONT_SIZE, 'Press "Space" to replay', const.BLACK_COLOR, 530)
    scoreTitle = ct.Content(const.SCORE_TITLE_FONT_URL, const.SCORE_TITLE_FONT_SIZE, 'SCORE', (235, 134, 52), const.WHD_2 - 60)
    BestTitle = ct.Content(const.SCORE_TITLE_FONT_URL, const.SCORE_TITLE_FONT_SIZE, 'BEST', (235, 134, 52), const.WHD_2)
    MedalTitle = ct.Content(const.SCORE_TITLE_FONT_URL, const.SCORE_TITLE_FONT_SIZE, 'MEDAL', (235, 134, 52), const.WHD_2 - 60)
    scoreContent = ct.ScoreContent(const.SCORE_FONT_URL, const.SCORE_FONT_SIZE, str(score.getScore()), const.WHITE_COLOR, const.WHD_2 - 35)
    BestContent = ct.ScoreContent(const.SCORE_FONT_URL, const.SCORE_FONT_SIZE, str(record), const.WHITE_COLOR, const.WHD_2 + 25)
    scoreTitle.setXplus(70)
    scoreContent.setXplus(70)
    BestTitle.setXplus(70)
    BestContent.setXplus(70)
    MedalTitle.setXminus(70)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    scoreTitle.setXminus(70)
                    scoreContent.setXminus(70)
                    BestTitle.setXminus(70)
                    BestContent.setXminus(70)
                    MedalTitle.setXplus(70)
                    so.die_sound.stop()
                    return
        fn.draws(background, columns, bird, sc.ScoreBoard(), lg.GameOverLogo(), goGuide, scoreTitle, scoreContent, BestTitle, BestContent, MedalTitle)
        fn.drawMedal(score.getScore())
        mscreen.draw(0)
        bird_y = bird.getY()
        bird.setY(bird_y + 8)
        bird.setAngle(-90)
        if bird.getY() >= 600 - bird.getHeight():
            bird.setY(600 - bird.getHeight())
        pygame.display.update()
        var.fpsClock.tick(const.FPS)
