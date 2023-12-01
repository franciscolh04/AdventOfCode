priorities = 0

# Read input
with open("2022/Day 3/day3.in", "r") as file:
    lines = [line.strip() for line in file.readlines()]

# Divide lines
for i in range(len(lines)):
    size = len(lines[i])
    lines[i] = [lines[i][0: (size//2)], lines[i][(size//2):]]

# Find same item in both compartments
for line in lines:
    for i in line[0]:
        for j in line[1]:
            if i == j:
                if i.islower():
                    priorities += ord(i) - ord("a") + 1
                else:
                    priorities += ord(i) - ord("A") + 27
                break
        else:
            continue
        break

print("Sum of priorities: " + str(priorities))
