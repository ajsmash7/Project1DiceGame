# Author: Ashley Johnson
# Program: Farkle Dice Game

# This is the main controller. Automated functions of rolls and scoring are in the Turn module.

import Turn

from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int
    turn_score: int
    turn: bool
    file: str

    print('''
                                              Let's Play Farkle! 
                                            First to 10,000 WINS!
        
                                *************** GAME RULES *******************
        
        Each Roll must score. Once a score of 500 is reached, a player can choose to stop rolling and keep the points, 
        or risk it all for more points. If a player does not score any points on a roll it is a bust; all points 
        lost and becomes the computer's turn
    
        Points are scored by rolling:
            1s               100
            5s                50
        3 of a kind      # of die x 100
        4 of a kind      3 of a kind x2
        5 of a kind      4 of a kind x2
        6 of a kind      5 of a kind x2
         
        Get all six 1s on the first roll for an INSTANT WIN!''')


    # assign players

player_name = input("What is your name?: ")
human = Player(player_name, 0, 0, True, 'player.txt')
computer = Player("Computer", 0, 0, False, 'computer.txt')
win = False

# While no one has 10,000 points, play the game.
while win == False:

    # initialize all 6 dice for first roll.
    comp_rolling = []
    human_rolling = []

    while human.turn:
        rolled_dice = Turn.roll(human_rolling)
        rolled_score = Turn.score(rolled_dice)

        print(human.name + "! You rolled: ")
        print(rolled_dice)

        if rolled_score == 0:
            print("\nBUST! Your turn is over")
            human.turn_score = 0
            computer.turn = True
            human.turn = False
            break

        print("\nCurrent Rolled Score: " + str(rolled_score))

        if rolled_score >= 500:
            keep = input("Do you want to keep this score, and end your turn?(y/n): ")
            keep.lower()
            if keep == "y":
                Turn.save(human.file, (rolled_score + human.turn_score))
                human.score = Turn.total(human.file)
                print("\n Your current score is: " + str(human.score))
                human.turn_score = 0
                computer.turn = True
                human.turn = False
                break

        str_dice = input("List the dice you'd like to keep, separated by comma: ")
        temp_dice = str_dice.split(',')
        saved_dice = [int(num) for num in temp_dice]
        human.turn_score += Turn.score(saved_dice)

        human_rolling = saved_dice

    while computer.turn:
        rolled_dice = Turn.roll(comp_rolling)
        rolled_score = Turn.score(rolled_dice)

        print(computer.name + " rolled: ")
        print(rolled_dice)

        if rolled_score == 0:
            print("\nBUST! Your turn is over")
            computer.turn_score = 0
            computer.turn = False
            human.turn = True
            break

        print("\nCurrent Rolled Score: " + str(rolled_score))

        if rolled_score >= 500:
            temp_score = rolled_score + computer.turn_score + computer.score

            if temp_score > human.score:
                Turn.save(computer.file, (rolled_score + computer.turn_score))
                computer.score = Turn.total(computer.file)
                print("\n Computer current score is: " + str(computer.score))
                computer.turn_score = 0
                computer.turn = False
                human.turn = True
                break

        comp_fin_score = Turn.score(rolled_dice)
        computer.turn_score = comp_fin_score

        comp_rolling = rolled_dice

    print("\n Current Scores: Player: " + str(human.score) + " Computer: " + str(computer.score))

    if human.score >= 10000:
        print("You won! Congratulations!")
        win = True
        Turn.endgame()
    if computer.score >= 10000:
        print("You lost. Better luck next time!")
        win = True
        Turn.endgame()