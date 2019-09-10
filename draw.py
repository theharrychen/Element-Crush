"""
Module for loading images and drawing all visual game elements
Images Used: https://www.deviantart.com/v-pk/art/Element-symbols-428049065
"""

import pygame, os

__author__ = "Harry Chen"
__email__ = "harry.chen1@ucalgary.ca"
__version__ = "0.1"

image_dict = {}

def load_images():
    image_names = ["fire", "air", "water", "earth", "light", "dark"]
    for i in range(len(image_names)):
        file_path = "images/" + image_names[i] + ".png"
        image_dict[image_names[i]] = pygame.image.load(file_path)

#Returns a pygame screen object
def create_screen(grid_width, grid_height, box_length):
    global BOX_LENGTH, screen
    BOX_LENGTH = box_length
    
    load_images()
    window_icon = image_dict["fire"]
    pygame.display.set_icon(window_icon)
    pygame.display.set_caption("Element Crush")

    screen = pygame.display.set_mode((BOX_LENGTH*(grid_width+2),
                                      BOX_LENGTH*grid_height))
    return screen

#Scales the smaller array length numbers to pixels
def to_pixels(x):
    return x*BOX_LENGTH

def window(board, turns_left, score, goal_score):
    screen.fill((255, 255, 255)) #Clears the screen to all white
    draw_sidebar(turns_left, score, goal_score)
    draw_board(board)

def draw_sidebar(turns_left, score, goal_score):
    font = pygame.font.SysFont("Times New Roman", 40)

    text = font.render("Goal:", True, (205,133,63))
    screen.blit(text, (to_pixels(7.25), to_pixels(0)))
    pygame.draw.line(screen, (205,133,63), (to_pixels(7), to_pixels(0.6)),#startpoint
                     (to_pixels(8.75),to_pixels(0.6)), 1) #endpoint, width
    text = font.render(str(goal_score), True, (205,133,63))
    screen.blit(text, (to_pixels(7.4), to_pixels(0.6)))

    text = font.render("Turns", True, (0,0,0))
    screen.blit(text, (to_pixels(7.2), to_pixels(1.5)))    
    text = font.render("Left:", True, (0,0,0))
    screen.blit(text, (to_pixels(7.3), to_pixels(2)))
    pygame.draw.line(screen, (0,0,0), (to_pixels(7), to_pixels(2.6)),
                     (to_pixels(8.75),to_pixels(2.6)), 1)
    text = font.render(str(turns_left), True, (0,191,255))
    screen.blit(text, (to_pixels(7.5), to_pixels(2.6)))

    text = font.render("SCORE:", True, (0,0,255))
    screen.blit(text, (to_pixels(7), to_pixels(3.5)))    
    pygame.draw.line(screen, (0,0,255), (to_pixels(7), to_pixels(4.1)),
                     (to_pixels(8.9),to_pixels(4.1)), 1)
    offset = 0
    if score >= 100: offset = -0.3
    elif score >= 10: offset = -0.15
    text = font.render(str(score), True, (255,0,0))
    screen.blit(text, (to_pixels(7.75 + offset), to_pixels(4.1)))

    text = font.render("Scoring:", True, (0,0,0))
    screen.blit(text, (to_pixels(7), to_pixels(5)))    
    pygame.draw.line(screen, (0,0,0), (to_pixels(7), to_pixels(5.6)),
                     (to_pixels(8.9),to_pixels(5.6)), 1)
    font = pygame.font.SysFont("Times New Roman", 12)
    text = font.render("Elements Matched in a Turn", True, (0,0,0))
    screen.blit(text, (to_pixels(7), to_pixels(5.7)))
    text = font.render("X", True, (0,0,0))
    screen.blit(text, (to_pixels(7.8), to_pixels(5.9)))  
    text = font.render("Turn Combo Count", True, (0,0,0))
    screen.blit(text, (to_pixels(7.25), to_pixels(6.1)))
    
def draw_board(board): 
    for y in range(len(board)):
        for x in range(len(board[y])):
            draw_icon(board[y][x], x, y)

#for loading and drawing each of the tiles
def draw_icon(num, x, y):
    icon = None
    x = to_pixels(x)+3 #box = 70x70, images are 64x64, pixel offset to center
    y = to_pixels(y)+3
    
    if num == 1:
        icon = image_dict["water"]
    elif num == 2:
        icon = image_dict["fire"]
    elif num == 3:
        icon = image_dict["air"]
    elif num == 4:
        icon = image_dict["earth"]
    elif num == 5:
        icon = image_dict["light"]
    elif num == 6:
        icon = image_dict["dark"]
    if num != 0:
        screen.blit(icon, (x,y))

def selected(x, y):
    x = to_pixels(x)
    y = to_pixels(y)
    rect = pygame.Rect(x, y, BOX_LENGTH, BOX_LENGTH)
    pygame.draw.rect(screen, (255,0,0), rect, 3)

def win():
    center_msg("WIN!")

def lose():
    center_msg("LOSE")

#draws win or lose msg in the center of the screen
def center_msg(msg):
    color = (0,0,0)
    if msg == "WIN!": color = (0,255,0)
    elif msg == "LOSE": color = (255,0,0)
    
    rect = pygame.Rect(to_pixels(2), to_pixels(3),
                              to_pixels(3), to_pixels(2))
    pygame.draw.rect(screen, (255,255,255), rect, 0)
    pygame.draw.rect(screen, color, rect, 4)
    font = pygame.font.SysFont("Times New Roman", 70)
    text = font.render("YOU", True, color)
    screen.blit(text, (to_pixels(2.4), to_pixels(3)))
    text = font.render(msg, True, color)
    screen.blit(text, (to_pixels(2.4), to_pixels(4)))

def combo_msg(combo_count):
    msg = ""
    color = (0,0,0)
    x = 0.1
    
    if combo_count >= 5:
        color = (255,0,0)
        msg = "LEGENDARY"
    elif combo_count == 4:
        color = (255,0,255)
        msg = "EPIC"
        x = 2.25
    elif combo_count == 3:
        color = (0,255,255)
        msg = "TRIPLE"
        x = 1.65
    elif combo_count == 2:
        color = (0,255,0)
        msg = "DOUBLE"
        x = 1.2
    
    rect = pygame.Rect(0, to_pixels(4), to_pixels(7), to_pixels(1))
    pygame.draw.rect(screen, (255,255,255), rect, 0)
    pygame.draw.rect(screen, color, rect, 4)

    font = pygame.font.SysFont("Times New Roman", 79)
    text = font.render(msg, True, color)
    screen.blit(text, (to_pixels(x), to_pixels(3.9)))
