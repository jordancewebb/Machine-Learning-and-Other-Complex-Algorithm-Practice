import pygame
import pygame.draw
import math
from queue import PriorityQueue

WIDTH = 800
Win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

RED = (255,0,0)
BLUE = (0,255,0)
GREEN = (0,0,255)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)
TURQOUISE = (64, 224, 208)
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.adjacents = []
        self.width = width
        self.total_rows = total_rows

    def getPosition(self):
        return self.row, self.col

    def isClosed(self):
        return self.color == RED

    def isOpen(self):
        return self.color == GREEN

    def isBarrier(self):
        return self.color == BLACK
    
    def isStart(self):
        return self.color == ORANGE

    def isEnd(self):
        return self.color == TURQOUISE
    
    def reset(self):
        return self.color == WHITE

    def makeClosed(self):
        self.color = RED

    def makeOpen(self):
        self.color = GREEN

    def makeBarrier(self):
        self.color = BLACK
    
    def makeStart(self):
        self.color = ORANGE

    def makeEnd(self):
        self.color = TURQOUISE

    def makePath(self):
        self.color = PURPLE

    def draw(self, Win):
        pygame.draw.rect(Win, self.color, (self.x, self.y, self.width, self.width))

    def update_adjacents(self):
        pass

    def __lt__(self, other):
        return False

def heuristicFunction(point1, point2):
    x1, y1 = point1
    x2, y2 = point2

    return abs(x1 - x2) + abs(y1 - y2)

def makeGrid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(i, j , gap, rows)
            grid[i].append(node)

    return grid

def drawGridLines(win, rows, width):
    GAP = width // rows
    for i in range(rows):
        pygame.draw.line(win, (128,128,128), (0, i*GAP), (width, i * GAP))
        print("i = ", i)
        for j in range(rows):
            pygame.draw.line(win, (128, 128, 128), (j*GAP, 0), (j * GAP, width))
            #print("j = ", j)

def draw(Win, grid, rows, width):
    Win.fill(RED)

    for row in grid:
        for node in row:
            node.draw(Win)

    drawGridLines(Win, rows, width)

def getClickedPosition(position, rows, width):
    gap = width // rows
    y, x = position

    row = y // gap
    col = x // gap
    return row, col

def main(Win, width):
    ROWS = 50
    grid = makeGrid(ROWS, width)

    start = None
    end = None

    run = True
    started = False
    Win.fill((255,0,0))
    while run:
        
        draw(Win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if started:
            continue

        if pygame.mouse.get_pressed()[0]:
            print("clicked")
            position = pygame.mouse.get_pos()
            row, col = getClickedPosition(position, ROWS, width)
            print(row,col)
            node = grid[row][col]
            if not start and node != end:
                start = node
                start.makeStart()
            elif not end:
                end = node
                end.makeEnd()
            
            elif node != end and node != start:
                node.makeBarrier()

        elif pygame.mouse.get_pressed()[2]:
            position = pygame.mouse.get_pos()
            row, col = getClickedPosition(position, ROWS, width)
            node = grid[row][col]
            node.reset()
            if node == start:
                start = None
            elif node == end:
                end = None
        #pygame.display.update()
    pygame.quit()

main(Win, WIDTH)