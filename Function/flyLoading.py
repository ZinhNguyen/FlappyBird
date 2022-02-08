
def flying(up, y, height):
    if up == True:
        y -= 0.5
    if up == False:
        y += 0.5
    if y == 361.5 - height:
        up = False
    if y == 361.5 + height:
        up = True
    return y, up