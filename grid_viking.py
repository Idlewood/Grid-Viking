import pygame, sys
from pygame.locals import *

screenWidth = 600
screenHeight = 600

pygame.init()

fpsClock = pygame.time.Clock()
FPS = 30

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
gridSize = 40
worldWidth = len(worldMap[0])
worldHeight = len(worldMap)

mainScreen = pygame.Surface((worldWidth * gridSize, worldHeight * gridSize))


dungeonFloor = pygame.image.load('sprites/dungeon_floor.png')
dungeonFloor = pygame.transform.scale(dungeonFloor, (gridSize, gridSize))

dungeonWall = pygame.image.load('sprites/dungeon_wall.png')
dungeonWall = pygame.transform.scale(dungeonWall, (gridSize, gridSize))


DISPLAYSURF = pygame.display.set_mode((screenWidth, screenHeight))

playPosition = [0, 0]

class Hero:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.sprite = pygame.image.load('sprites/viking.png')
        self.sprite = pygame.transform.scale(self.sprite, (gridSize, gridSize))
        
    def drawHero(self, surface):
        surface.blit(self.sprite, (self.x * gridSize, self.y * gridSize))

    def moveHero(self, direction):

        global worldMap
        if direction == 'up':
            if self.isValidMove(self.y - 1, self.x, worldMap):
                self.y = self.y - 1
        if direction == 'down':
            if self.isValidMove(self.y + 1, self.x, worldMap):
                self.y = self.y + 1
        if direction == 'left':
            if self.isValidMove(self.y, self.x - 1, worldMap):
                self.x = self.x - 1
        if direction == 'right':
            if self.isValidMove(self.y, self.x + 1, worldMap):
                self.x = self.x + 1

    def isValidMove(self, x, y, worldMap):
        mapBoundaryX = len(worldMap)
        mapBoundaryY = len(worldMap[0])
        if x in range(0,mapBoundaryX) and y in range(0,mapBoundaryY):
            if worldMap[x][y] == 1:
                return True
            else:
                return False
        else:
            return False



ourHero = Hero((0,0))


def makeBorder(worldMap):
    worldWidth = len(worldMap[0]) * gridSize
    worldHeight = len(worldMap) * gridSize
    pygame.draw.line(DISPLAYSURF, gridColor, (0,0), (worldWidth, 0), 1)
    pygame.draw.line(DISPLAYSURF, gridColor, (worldWidth,0), (worldWidth, worldHeight), 1)

def makeWall(x1, y1):
    mainScreen.blit(dungeonWall, (x * gridSize, y * gridSize))
def drawPlayer(playPosition):
    x = playPosition[1]
    y = playPosition[0]
    mainScreen.blit(viking, (x * gridSize, y * gridSize)) 



while True:
    
    DISPLAYSURF.fill(BLACK)
    # print "x: %s y: %s" % (playPosition[0], playPosition[1])
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
                if event.key == K_DOWN:
                    ourHero.moveHero('down')
                if event.key == K_UP:
                    ourHero.moveHero('up')
                if event.key == K_RIGHT:
                    ourHero.moveHero('right')
                if event.key == K_LEFT:
                    ourHero.moveHero('left')

    
    
    
    for y in range(0, len(worldMap)):
        for x in range(0, len(worldMap[y])):
                mainScreen.blit(dungeonFloor, (x * gridSize, y * gridSize))
    for y in range(0, len(worldMap)):
        for x in range(0, len(worldMap[y])):
                if worldMap[y][x] == 2:
                    makeWall(x * gridSize, y * gridSize)
    #drawPlayer(playPosition)
    ourHero.drawHero(mainScreen)
    DISPLAYSURF.blit(mainScreen, (30, 30))      
    pygame.display.update()
    fpsClock.tick(FPS)
