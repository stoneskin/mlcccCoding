# SmileyMove.py
import pygame                # Setup
pygame.init()
screen = pygame.display.set_mode([600,600])
keep_going = True
pic = pygame.image.load("images/CrazySmile.bmp")


# the color key is to make the image looks better when move,
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)

#  change the value of  picx and picy to control image position. so the image looks is moving
picx = 0
picy = 0
BACKColor = (50, 60, 90) # background color
screen.fill(BACKColor)
timer = pygame.time.Clock()  # Timer for animation


while keep_going:            # Game loop
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            keep_going = False
    picx += 1                # Move the picture
    picy += 1
    screen.fill(BACKColor)   # Refill the background color, try comment this to see different
    screen.blit(pic, (picx, picy))
    pygame.display.update()

    timer.tick(60)           # Limit to 60 frames per second
pygame.quit()                # Exit

