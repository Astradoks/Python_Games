import pygame
import random
pygame.init()

class Snake(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 10
        self.velocity = 10
        self.directionX = 1
        self.directionY = 0

    def move(self, keys):
        
        if keys[pygame.K_RIGHT] and self.directionX != -1:
            self.directionX = 1
            self.directionY = 0

        if keys[pygame.K_LEFT] and self.directionX != 1:
            self.directionX = -1
            self.directionY = 0

        if keys[pygame.K_UP] and self.directionY != 1:
            self.directionX = 0
            self.directionY = -1

        if keys[pygame.K_DOWN] and self.directionY != -1:
            self.directionX = 0
            self.directionY = 1

        #Constant move of the snake
        self.x += self.directionX * self.velocity
        self.y += self.directionY * self.velocity

class Collectable(object):
    def __init__(self):
        self.radius = 5
        self.x = random.randrange(5, sizeX - self.radius, 10)
        self.y = random.randrange(5, sizeY - self.radius, 10)
        self.color = (200, 255, 0)

    def drawCollectable(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

#Game draw and update
def draw(win, completeSnake):
    win.fill((0, 0, 0))
    for snakeBlock in completeSnake:
        pygame.draw.rect(win, (0, 165, 255), (snakeBlock.x, snakeBlock.y, snakeBlock.width, snakeBlock.height))
    food.drawCollectable(win)
    pygame.display.update()

#Window declaration
sizeX = 500
sizeY = 500
win = pygame.display.set_mode((sizeX, sizeY))
pygame.display.set_caption("Sanke Game")
clock = pygame.time.Clock()

#Snake declaration
snakeBlock = Snake(250, 250)
count =  0
completeSnake = [snakeBlock]

#Collectable declaration
food = Collectable()

#Loop for the game
run = True
while run:

    #A lite delay between every frame
    clock.tick(10)

    #Look for all the events that ocurre in the game
    for event in pygame.event.get():
        #Event to close the game
        if event.type == pygame.QUIT:
            run = False
    
    #Get of the keys that are pressed
    keys = pygame.key.get_pressed()
    
    #Refresh all the blocks of the snake
    if len(completeSnake) > 1:
        for i in range(len(completeSnake) - 1, -1, -1):
            if i != 0:
                completeSnake[i].x = completeSnake[i-1].x
                completeSnake[i].y = completeSnake[i-1].y

    #Move of the snake
    snakeBlock.move(keys)

    #Collection of food
    if food.x < snakeBlock.x + snakeBlock.width and food.x > snakeBlock.x:
        if food.y < snakeBlock.y + snakeBlock.height and food.y > snakeBlock.y:
            lastX = completeSnake[count].x
            lastY = completeSnake[count].y
            completeSnake.append(Snake(lastX, lastY))
            food = Collectable()
            count += 1

    #infinite move through the walls
    if snakeBlock.x < 0:
        snakeBlock.x = sizeX - snakeBlock.width
    if snakeBlock.x > sizeX - snakeBlock.width:
        snakeBlock.x = 0
    if snakeBlock.y < 0:
        snakeBlock.y = sizeY - snakeBlock.height
    if snakeBlock.y > sizeY - snakeBlock.height:
        snakeBlock.y = 0

    #Window update
    draw(win, completeSnake)

pygame.quit()