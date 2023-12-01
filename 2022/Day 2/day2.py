# CONSTANTS
ROCK = 1
PAPER = 2
SCISSORS = 3

DRAW = 3
WIN = 6

# ALL POSSIBLE PLAYS
dic = {"A": ROCK, "B": PAPER, "C": SCISSORS,
       "X": ROCK, "Y": PAPER, "Z": SCISSORS}

myScore = 0

# Read input
with open("2022/Day 2/day2.in", "r") as file:
    lines = [line.split() for line in file.readlines()]

# Decide what to play
for line in lines:
    # Need to lose
    if line[1] == "X":
        if dic[line[0]] == ROCK:
            line[1] = "C"
        elif dic[line[0]] == PAPER:
            line[1] = "A"
        else:
            line[1] = "B"
    # Need to draw
    elif line[1] == "Y":
        line[1] = line[0]
    # Need to win
    else:
        if dic[line[0]] == ROCK:
            line[1] = "B"
        elif dic[line[0]] == PAPER:
            line[1] = "C"
        else:
            line[1] = "A"

# Calculate round score
for line in lines:
    # Add shape value
    myScore += dic[line[1]]
    round = (dic[line[0]], dic[line[1]])

    if round[0] != round[1]:
        # Victory
        if (round == (ROCK, PAPER) or round == (PAPER, SCISSORS) or round == (SCISSORS, ROCK)):
            myScore += WIN
    else:
        # Draw
        myScore += DRAW

print("My score: " + str(myScore))