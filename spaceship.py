#!/usr/bin/python3

import time
import random
import subprocess

build_material = '#'
smoke_material = '*'
smoke_lines = 3
max_space_between_ships = 30


def center_spaceship(width: int, qty: int):
    delta = width - qty
    filler = ''
    for x in range(1, int(delta / 2) + 1):
        filler = filler + ' '
    spaceshipline = build_material * qty
    line = '{}{}{} '.format(filler, spaceshipline, filler)
    return line


def right_shift(max_width: int):
    offset = ' '
    max_shift = int(columns) - max_width
    if max_shift > 0:
        for x in range(1, random.randint(1, max_shift)):
            offset = offset + ' '
    return offset


def add_smoke(max_width: int, offset: str):
    smoke = ' '
    for x in range(1, max_width - 2):
        smoke = smoke + smoke_material
    smoke = smoke + ' '
    for x in range(1, smoke_lines + 1):
        print('{}{}'.format(offset, smoke))


def spaceship(max_width=30):
    for spaceshipline in range(1, (max_width + 1), 2):
        print('{}{}'.format(right_offset, center_spaceship(max_width, spaceshipline)))
        time.sleep(.1)


def spacing(space_between_ships=30):
    for roll in range(1, random.randint(1, space_between_ships)):
        print('')
        time.sleep(.2)


# Lead with some space before showing spaceships.
spacing()

while True:
    """
    To adust for changing terminal window sizes grab the console window size each cycle.
    Note: If you go from a larger terminal window to a smaller one the current spaceship
    might word wrap in the new terminal size.
    """
    rows, columns = subprocess.check_output(['stty', 'size']).decode().split()
    max_spaceship_width = int(int(columns) / 3)

    # Set the maximum width for this spaceship
    spaceship_max_width = random.randint(1, max_spaceship_width) * 3

    # Offset the spaceship from the left margin
    right_offset = right_shift(max_width=spaceship_max_width)

    # Build the spaceship
    spaceship(max_width=spaceship_max_width)

    # Add smoke to the underside of the spaceship
    add_smoke(max_width=spaceship_max_width, offset=right_offset)

    # Add spacing between spaceships
    spacing(space_between_ships=max_space_between_ships)
