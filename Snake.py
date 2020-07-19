import pygame
pygame.init()

#Window declaration
sizeX = 500
sizeY = 500
win = pygame.display.set_mode((sizeX, sizeY))
pygame.display.set_caption("Sanke Game")

#Snake declaration
x = 250
y = 250
height = 10
width = 10

#Some Variables Declaration
velocity = 10
directionX = 1
directionY = 0

#Loop for the game
game = True
while game:

    #A lite delay between every frame
    pygame.time.delay(50)

    #Look for all the events that ocurre in the game
    for event in pygame.event.get():
        #Event to close the game
        if event.type == pygame.QUIT:
            game = False
    
    #Get of the keys that are pressed
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        directionX = 1
        directionY = 0

    if keys[pygame.K_LEFT]:
        directionX = -1
        directionY = 0

    if keys[pygame.K_UP]:
        directionX = 0
        directionY = -1

    if keys[pygame.K_DOWN]:
        directionX = 0
        directionY = 1

    #Constant move of the snake
    x += directionX * velocity
    y += directionY * velocity

    #infinite move through the walls
    if x < 0:
        x = sizeX - width
    if x > sizeX - width:
        x = 0
    if y < 0:
        y = sizeY - height
    if y > sizeY - height:
        y = 0
    
    #Window update
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 165, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()