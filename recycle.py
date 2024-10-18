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
STARTSPEED = 10
FINAL_LEVEL = 9
# Why did I not do 10 levels? It is because the 9th one is already extremely hard!
ITEMS = ["battery","bottle","chips","plasticbag"]

game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def display_message(heading, subheading):
    screen.draw.text(heading, fontsize = 60, color = "black", center = CENTRE)
    screen.draw.text(subheading, fontsize = 30, color = "black", center = (350,350))
    
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


def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)

def make_items(number_of_extra_items):
    items_to_create = get_options_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_options_to_create(number_of_extra_items):
    items_to_create = ["paperbag"]
    for i in range(number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create
    
def create_items(items_to_create):
    x = []
    for option in items_to_create:
        y = Actor (option + "ing")
        x.append(y)
    return x

# Part 2
def layout_items(items_to_layout):
    number_of_gaps = len(items_to_layout) +1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(items_to_layout)
    for index,i in enumerate(items_to_layout):
        new_x_pos = (index+1) * gap_size
        i.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for i in items_to_animate:
        dur = STARTSPEED - current_level
        i.anchor = ("center","bottom")
        animation = animate(i,duration = dur, on_finished = handle_game_over, y = HEIGHT)
        animations.append(animation)

def handle_game_over():
    global game_over
    game_over = True

    # Part 3


def on_mouse_down(pos):
    global items, current_level
    for item in items:
        if item.collidepoint(pos):
            if "paperbag" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global items, current_level, animations, game_complete
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()


pgzrun.go()
