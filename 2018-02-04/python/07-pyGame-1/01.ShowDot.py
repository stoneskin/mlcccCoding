# ShowDot.py
# this script is show how to initial a pygame and draw a circle on tha page
import pygame

# initial the game
pygame.init()
screen = pygame.display.set_mode([800, 600])

# boolean flag to use control game run or quit
keep_going = True

# some data defined for game to use
GREEN = (0, 255, 0)  # RGB color triplet for GREEN
radius = 50

# only when keep_going is true, the game will running
while keep_going:
    # bellow code is for quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False
    # below code is for draw a circle in the screen
    pygame.draw.circle(screen, GREEN, (100, 100), radius)

    # refresh the screen displa
    pygame.display.update()

pygame.quit()
