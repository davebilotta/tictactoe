import pygame, sys, ai
from pygame.locals import *
from pygame import Color, Rect, Surface

# set up pygame
pygame.init()

# set up the window
WINDOWWIDTH = 700
WINDOWHEIGHT = 700
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Tic Tac Toe')

# Init board as all zeros 
board = [[0,0,0],[0,0,0],[0,0,0]]

BLACK = (0,0,0)
WHITE = (255,255,255)
ORANGE = (255,127,36)

# Display some text
background = pygame.Surface(screen.get_size())
background = background.convert()

font = pygame.font.Font(None,64)
fontLarge = pygame.font.Font(None,200)

screen.blit(background, (0, 0))
pygame.display.flip()

def setup():
    #
    # Does nothing for now 
    # 
    return True

def renderGame():
    #
    # Render grid 
    #
    lineWidth = WINDOWWIDTH * 0.70
    lineHeight = WINDOWHEIGHT * 0.70
    thickness = 20

    xStart = (WINDOWWIDTH - lineWidth - (thickness * 2))/2
    xOff = (lineWidth + (thickness * 2))/3

    yStart = (WINDOWHEIGHT - lineHeight - (thickness * 2))/2
    yOff = (lineHeight + (thickness * 2))/3

    # Horizontal lines
    pygame.draw.line (screen, (0,0,0), (xStart,(yStart + yOff)), ((xStart + lineWidth + thickness * 2),(yStart + yOff)), thickness)
    pygame.draw.line (screen, (0,0,0), (xStart,(yStart + yOff * 2)), ((xStart + lineWidth + thickness * 2),(yStart + yOff * 2)), thickness)

    # Vertical lines
    pygame.draw.line (screen, (0,0,0), ((xStart + xOff),yStart), ((xStart + xOff),(yStart + lineHeight + thickness * 2)), thickness)
    pygame.draw.line (screen, (0,0,0), ((xStart + xOff * 2),yStart), ((xStart + xOff * 2),(yStart + lineHeight + thickness * 2)), thickness)

    #
    # Render board
    # 
    X = fontLarge.render("X", 1, BLACK)
    O = fontLarge.render("O", 1, BLACK)
    
    for y in range(0,3):
        for x in range(0,3):
            xPos = xStart + (xOff * y) + (thickness * 2 * y)
            yPos = yStart + (yOff * x) + (thickness * 2 * x)
            #print board

            if (board[x][y] == 'X'):
                screen.blit(X,(xPos,yPos))

            elif (board[x][y] == 'O'):
                screen.blit(O,(xPos,yPos))
            
            #screen.blit(fontLarge.render(board[x][y],1,BLACK),(xPos,yPos))

setup()

while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            print event.key

            if event.key == pygame.K_ESCAPE: 
                pygame.quit()
                sys.exit()

    screen.fill(ORANGE)

    renderGame()

    pygame.display.update()
   