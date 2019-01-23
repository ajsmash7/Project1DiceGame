# Ashley Johnson
# A separate module for the functions of a single turn of a player

import random
from dataclasses import dataclass


@dataclass
class Die:
    index: int
    value: int

# define a simple function to roll and return one dice.


def roll_die():
    one_die = random.randint(1, 6)
    return one_die


def score(current_roll):
    sets_score = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}

    multiplier = {4: 2, 5: 3, 6: 4}

    die_score = {1: 100, 2: 0, 3: 0, 4: 0, 5: 50, 6: 0}

    dice_score = 0

    dice_roll = current_roll
    match = []
    dice_left = []
    no_score = []

    auto_win = [1, 1, 1, 1, 1, 1]
    straight = [1, 2, 3, 4, 5, 6]


    # if there are 6 dice, check if it is an automatic win, if so return 100000 to signal auto win
    if dice_roll == auto_win:
        return 100000
    # if not ten thousand, then check for a straight.
    if dice_roll == straight:
        return 1500

    # check for 3 or more of a kind using a nested loop. The outer loop checks each die value against the inner loop of
    # dice rolls. If the roll matches the die number,

    for a in dice_roll:
        match = [b for b in dice_roll if b.value == a.value]


    # based on quantity of matches
    match_qty = len(match)
    match_val = match[0]
    print(match_val)

    if match_qty > 3:
        dup_score = sets_score.get(match_val)
        dup_multi = multiplier.get(match_qty)
        dice_score += dup_score*dup_multi
        dice_left = [c for c in dice_roll if c.value != match_val]

    for e in dice_left:
        single_val = die_score.get(e.value)
        if single_val > 0:
            dice_score += single_val
        else:
            no_score += [e.value]

    return dice_score, no_score


def roll(num_of_dice):

    # determine number of dice to be rolled based on how many dice were saved
    to_roll = (6 - (len(num_of_dice)))

    # declare a blank list to assign the new dice rolls to, if it is their first roll assign blank to current roll.
    another_roll = []

    # loop through each die roll
    for f in range(to_roll):
        another_roll += [roll_die()]

    another_roll.sort()
    g = 0
    d_roll = []

    for j in another_roll:
        new_die = Die(g, j)
        d_roll += [new_die]
        g += 1

    return d_roll, another_roll


def save(filename, addScore):
    save_file = open(filename, 'a')
    save_file.write(str(addScore) + '\n')
    save_file.close()


def total(filename):
    open_file = open(filename, 'r')
    game_total = 0
    score_list = open_file.readlines()
    num_scores = len(score_list)
    open_file.close()

    for k in range(num_scores):
        cur_score = int(score_list[k])
        game_total += cur_score

    return game_total


def endgame():
    open('player.txt', 'w').close()
    open('computer.txt', 'w').close()