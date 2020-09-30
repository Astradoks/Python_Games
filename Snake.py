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

    def collition(self, snakeBlock):
        if self.x >= snakeBlock.x and self.x + self.width <= snakeBlock.x + snakeBlock.width:
            if self.y >= snakeBlock.y and self.y + self.height <= snakeBlock.y + snakeBlock.height:
                return True

class Collectable(object):
    def __init__(self):
        self.radius = 5
        self.x = random.randrange(5, sizeX - self.radius, 10)
        self.y = random.randrange(55, sizeY - self.radius, 10)
        self.color = (200, 255, 0)

    def drawCollectable(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

#Game draw and update
def draw(win, completeSnake):
    win.fill((0, 0, 0))

    #Draw the snake
    for snakeBlock in completeSnake:
        pygame.draw.rect(win, (0, 165, 255), (snakeBlock.x, snakeBlock.y, snakeBlock.width, snakeBlock.height))
    
    #Draw the food
    food.drawCollectable(win)

    #Print score
    score = fontScore.render('Score: ' + str(count), True, (255, 255, 255))
    scoreRect = score.get_rect()
    scoreRect.center = (70, 30)
    win.blit(score, scoreRect)

    #Print end text when you die
    endTextRect = endText.get_rect()
    endTextRect.center = (sizeX // 2, sizeY // 2)
    win.blit(endText, endTextRect)

    #Print restart text
    restartTextRect = restartText.get_rect()
    restartTextRect.center = (sizeX // 2, (sizeY // 2) + 30)
    win.blit(restartText, restartTextRect)

    #Refresh the screen
    pygame.display.update()

#Window declaration
sizeX = 500
sizeY = 500
win = pygame.display.set_mode((sizeX, sizeY))
pygame.display.set_caption("Sanke Game")

#Refresh of the window
clock = pygame.time.Clock()
fps = 10

#Text for score and the end of the game
fontScore = pygame.font.Font('freesansbold.ttf', 24)
score = fontScore.render('', True, (255, 255, 255))
fontEnd = pygame.font.Font('freesansbold.ttf', 36)
endText = fontEnd.render('', True, (255, 255, 255))
fontRestart = pygame.font.Font('freesansbold.ttf',16)
restartText = fontRestart.render('', True, (255, 255, 255))

#Snake declaration
snakeBlock = Snake(250, 250)
completeSnake = [snakeBlock]

#Collectable declaration
food = Collectable()
count =  0

#Stop the game when you lose
lose = False

#Loop for the game
run = True
while run:

    #A lite delay between every frame
    clock.tick(fps + count)

    #Get of the keys that are pressed
    keys = pygame.key.get_pressed()

    #Look for all the events that ocurre in the game
    for event in pygame.event.get():
        #Event to close the game
        if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
            run = False 

    #Stop the game when you lose
    if lose:
        if keys[pygame.K_r]:
            #Restart of al the variables
            snakeBlock = Snake(250, 250)
            completeSnake = [snakeBlock]
            food = Collectable()
            count =  0
            score = fontScore.render('', True, (255, 255, 255))
            endText = fontEnd.render('', True, (255, 255, 255))
            restartText = fontRestart.render('', True, (255, 255, 255))
            lose = False
    else:
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

        #Check for collition in each block of the snake
        if count > 1:
            for block in completeSnake[1:]:
                if snakeBlock.collition(block):
                    endText = fontEnd.render('Game Over', True, (255, 255, 255))
                    restartText = fontRestart.render('Press r to restart', True, (255, 255, 255))
                    lose = True

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