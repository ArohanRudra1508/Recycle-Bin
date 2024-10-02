# Part 1

import pgzrun
import random

FONT_White = (255,255,255)
TITLE = "Recycling Game"
WIDTH = 800
HEIGHT = 600
CENTREx = WIDTH/2
CENTREy = HEIGHT/2
CENTRE = CENTREx,CENTREy
STARTSPEED = 5
FINAL_LEVEL = 10
ITEMS = ["battery","bottle","chips","plasticbag"]

game_over = false
game_complete = false
current_level = 1
items = []
animations = []

# Part 2
def display_message(heading, subheading):
    screen.draw.text(heading, fontsize = 60, color = "black", centre = CENTRE)
    screen.draw.text(subheading, fontsize = 30, color = "black" centre = 350,350)
#Part 3 
    
def draw():
    global items, current_level, game_over, game_complete
    screen.clear()
    screen.blit("backgrounding",(0,0))
    if game_over:
        display_message("You failed the recycling test!","Please try again later!")
    elif game_complete:
        display_message("You passed the recycling test!", "Congratulate yourself!")
    else:
        for item in items:
            item.draw()

def get_options_to_create(extra_items):
    items_to_create = ["paperbag"]
    for i in range(0,extra_items):
        random_option = random.choice[ITEMS]
        items_to_create.append(random_option)
    return items_to_create
    
def create_items(items_to_create):
    x = []
    for option in items_to_create:
        y = Actor (option + "ing")
        x.append(y)
    return x

# Part 4














































































pgzrun.go()
