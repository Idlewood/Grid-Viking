import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))

WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREY  = (100, 100, 100)


worldMap = [ [1, 1, 1, 1, 1, 1, 1],\
             [1, 1, 2, 2, 1, 1, 1],\
             [1, 1, 2, 1, 1, 1, 1],\
             [1, 1, 2, 1, 1, 1, 1] ]

gridColor = GREY
gridSize = 30
worldWidth = len(worldMap[0])
worldHeight = len(worldMap)


DISPLAYSURF = pygame.display.set_mode((worldWidth * gridSize + 1, worldHeight * gridSize + 1))
# One pixel is added to the top and side to accomodate the grid line

playPosition = [0, 0]



def isValidMove(x, y, worldMap):
    mapBoundaryX = len(worldMap)
    mapBoundaryY = len(worldMap[0])
    if x in range(0,mapBoundaryX) and y in range(0,mapBoundaryY):
        if worldMap[x][y] == 1:
            return True
        else:
            return False
    else:
        return False

def movePlayer(direction):
    global worldMap
    global playPosition
    if direction == 'up':
        if isValidMove(playPosition[0] - 1, playPosition[1], worldMap):
            playPosition[0] = playPosition[0] - 1
    if direction == 'down':
        if isValidMove(playPosition[0] + 1, playPosition[1], worldMap):
            playPosition[0] = playPosition[0] + 1
    if direction == 'left':
        if isValidMove(playPosition[0], playPosition[1] - 1, worldMap):
            playPosition[1] = playPosition[1] - 1
    if direction == 'right':
        if isValidMove(playPosition[0], playPosition[1] + 1, worldMap):
            playPosition[1] = playPosition[1] + 1


def makeGrid(x1, y1):
    pygame.draw.line(DISPLAYSURF, gridColor, (x1, y1), (x1, y1 + gridSize), 1)
    pygame.draw.line(DISPLAYSURF, gridColor, (x1, y1 + gridSize), (x1 + gridSize, y1 + gridSize), 1)
def makeBorder(worldMap):
    worldWidth = len(worldMap[0]) * gridSize
    worldHeight = len(worldMap) * gridSize
    pygame.draw.line(DISPLAYSURF, gridColor, (0,0), (worldWidth, 0), 1)
    pygame.draw.line(DISPLAYSURF, gridColor, (worldWidth,0), (worldWidth, worldHeight), 1)

def makeWall(x1, y1):
    pygame.draw.rect(DISPLAYSURF, RED, (x1, y1, gridSize, gridSize))
def drawPlayer(playPosition):
    x = playPosition[1]
    y = playPosition[0]
    pygame.draw.rect(DISPLAYSURF, GREEN, (x * gridSize, y * gridSize, gridSize, gridSize))

while True:
    



    DISPLAYSURF.fill(BLACK)
    print "x: %s y: %s" % (playPosition[0], playPosition[1])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    movePlayer('down')
                if event.key == K_UP:
                    movePlayer('up')
                if event.key == K_RIGHT:
                    movePlayer('right')
                if event.key == K_LEFT:
                    movePlayer('left')

    
    for y in range(0, len(worldMap)):
        for x in range(0, len(worldMap[y])):
                if worldMap[y][x] == 2:
                    makeWall(x * gridSize, y * gridSize)
    drawPlayer(playPosition)
    for y in range(0, len(worldMap)):
        for x in range(0, len(worldMap[y])):
                makeGrid(x * gridSize, y * gridSize)
           
    makeBorder(worldMap)
    pygame.display.update()
