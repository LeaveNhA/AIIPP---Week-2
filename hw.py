# required modules;
import random
import re

# Business Logic;
# https://youtu.be/7mOBWHh1soY?t=544 Mathematical model of RPSLSp.

piece_matrix = ["rock", "paper", "scissors", "lizard", "Spock"]

player_choose_text = 'Player chooses '
computer_choose_text = 'Computer chooses '


def name_to_number(name):
    return piece_matrix.index(name);

def number_to_name(number):
    return piece_matrix[number];

def choose():
    return random.randrange(0, 4)

def winner(player, computer):
    winner_matrix = [[0, -1, 1, 1, -1],
                    [1, 0, -1, -1, 1],
                    [-1, 1, 0, 1, -1],
                    [-1, 1, -1, 0, 1],
                    [1, -1, 1, -1, 0]];
    result = winner_matrix[player][computer];
    return "Computer wins!" if result == -1 else ("Player wins!" if (result == 1) else "Player and computer tie!")

def to_winner(i):
    return "Player" if i == 2 else ("Computer" if i == 1 else "Nobody")

def rpsls(player_choice):
    computer_choice = choose()

    print(player_choose_text + player_choice)

    print(computer_choose_text + number_to_name(computer_choice))

    print(winner(int(name_to_number(player_choice)), computer_choice))
    print("")

# Essential calls to test program!
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
