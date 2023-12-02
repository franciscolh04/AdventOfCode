# CONSTANTS
RED = 12
GREEN = 13
BLUE = 14

sum = 0

# Read input
with open("2023/Day 2/day2.in", "r") as file:
    lines = [line.split(":") for line in file.readlines()]

for line in lines:
    game = {"red": 0, "green": 0, "blue": 0}
    power = 1

    # Divide in sets
    line[1] = line[1].split(";")
    for set in range(len(line[1])):
        # Divide in pairs
        line[1][set] = line[1][set].split(",")
        for pair in range(len(line[1][set])):
            line[1][set][pair] = line[1][set][pair].split()
            # Add colours
            if "red" in line[1][set][pair]:
                game["red"] = max(game["red"], int(line[1][set][pair][0]))
            if "green" in line[1][set][pair]:
                game["green"] = max(game["green"], int(line[1][set][pair][0]))
            if "blue" in line[1][set][pair]:
                game["blue"] = max(game["blue"], int(line[1][set][pair][0]))
        
    
    # Get the power of the set and add it to the sum
    for colour in game.values():
        power *= colour

    sum += power

print(sum)