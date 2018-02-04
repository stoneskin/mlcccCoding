# ShowPic.py
# this script is demo how to load a image to the pygame screen

import pygame  # Setup

pygame.init()
screen = pygame.display.set_mode([800, 600])
keep_going = True

# define the picture path and name, it in same location of the script
pic = pygame.image.load("images/CrazySmile.bmp")

while keep_going:  # Game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False

    # blit() method will load the image from hard disk.  position will be (x,y)
    screen.blit(pic, (100, 100))

    pygame.display.update()

pygame.quit()  # Exit
