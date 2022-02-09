from Function import checkCollision as co
from Image import screen as sc
from Sound import start as st

WINDOWHEIGHT = sc.WINDOWHEIGHT

# Check GameOver
def isGameOver(bird, columns):
    for i in range(3):
        rectBird = [bird.x, bird.y, bird.width, bird.height]
        rectColumn1 = [columns.ls[i][0], columns.ls[i][1] - columns.height, columns.width, columns.height]
        rectColumn2 = [columns.ls[i][0], columns.ls[i][1] + columns.blank, columns.width, columns.height]
        if co.rectCollision(rectBird, rectColumn1) == True or co.rectCollision(rectBird, rectColumn2) == True:
            st.hit_sound.play()
            return True
    #if bird.y + bird.height < 0 or bird.y + bird.height > WINDOWHEIGHT - 160:
    if bird.y + bird.height > WINDOWHEIGHT - 160:
        return True
    return False
