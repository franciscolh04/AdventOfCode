# CONSTANTS
RED = 12
GREEN = 13
BLUE = 14

sum_ids = 0

# Read input
with open("2023/Day 2/day2.in", "r") as file:
    lines = [line.split(":") for line in file.readlines()]

for line in lines:
    possible = True

    # Divide in sets
    line[1] = line[1].split(";")
    for set in range(len(line[1])):
        # Divide in pairs
        line[1][set] = line[1][set].split(",")
        for pair in range(len(line[1][set])):
            line[1][set][pair] = line[1][set][pair].split()
            # Check if each pair is possible or not
            if ("red" in line[1][set][pair] and int(line[1][set][pair][0]) > RED) or \
               ("green" in line[1][set][pair] and int(line[1][set][pair][0]) > GREEN) or \
               ("blue" in line[1][set][pair] and int(line[1][set][pair][0]) > BLUE):
                possible = False
    
    # Verify if game is possible
    if possible:
        # Get game ID and add it to the sum
        sum_ids += int((line[0].split())[1])

print(sum_ids)