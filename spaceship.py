#!/usr/bin/python3

import time
import random

max_width = 30
build_material = '#'
smoke_material = '*'
smoke_lines = 3
space_between_ships = 30

def center_spaceship(width, qty):
    delta = width - qty
    filler = ''
    for x in range(1, int(delta / 2) + 1):
        filler = filler + ' '
    spaceship = build_material * qty
    line = '{}{}{} '.format(filler, spaceship, filler)
    return line

while(1):
    right_shift = ' '
    for x in range(1,random.randint(1,100)):
        right_shift = right_shift + ' '

    spaceship_width = random.randint(1,20) * 3
    for spaceshipline in range(1,(spaceship_width + 1), 2):
        print('{}{}'.format(right_shift, center_spaceship(spaceship_width, spaceshipline)))
        time.sleep(.1)

    smoke = ' '
    for x in range(1, spaceship_width - 2):
        smoke = smoke + smoke_material
    smoke = smoke + ' '
    for x in range(1, smoke_lines + 1):
        print('{}{}'.format(right_shift,smoke))

    for roll in range(1,random.randint(1,space_between_ships)):
        print('')
        time.sleep(.1)
