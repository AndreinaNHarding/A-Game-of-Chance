"""Simulation of the game craps"""
import random

def start_game():
    """Short Game introduction"""
    print('*-'*45)
    print("\n Welcome to the game, lets start playing Craps! \n")
    print('*-'*45)

def roll_dice():
    """Roll two dice and return face values into a tuple"""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return die1, die2

def display_dice(dice):
    """Receive a tuple, turns apart the tuple values and display the content """
    die1, die2 = dice
    print(f'Dice 1: {die1}{"Dice 2: ":>15}{die2} {"sum= ":>15}{sum(dice)}')

def game_status(sum_dice):
    if sum_dice in (7, 11):
        game_status = 'WON'
    elif sum_dice in(2, 3, 12):
        game_status = 'LOST'
    else:
        game_status = 'CONTINUE'
    return game_status


#Game Starts!
start_game() #--------------------------------Introduction of game
print("\n1st Roll: \n")
dice_values = roll_dice() #-------------------First roll of dice
display_dice(dice_values)

#determine sum of the values to define status of game:
sum_dice = sum(dice_values)

game_status = game_status(sum_dice)

if game_status == 'CONTINUE':
    point = sum_dice
    print("\nYou have a point, the value now is: {}\n".format(point))
   
    while game_status == 'CONTINUE':
        dice_values = roll_dice()
        display_dice(dice_values)
        if sum(dice_values) != 7:
            if sum(dice_values) == point:
                game_status = 'WON' #Player Wins
            else:
                   game_status = 'CONTINUE'
        else:
            game_status = 'LOST' #Player lost

#Displaying message for winning or loosing:
if game_status == 'WON':
    print('\nCONGRATS! You won the Game!!\n')
else:
    print('\nCRAPS! Sorry, you lost the Game\n')