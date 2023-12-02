calibration = 0
number = 0

# Read input
with open("2023/Day 1/day1.in", "r") as file:
    lines = [line.strip() for line in file.readlines()]

for line in lines:
    size = len(line)

    # Finds number from the beginning of the string
    for i in range(size):
        if line[i].isnumeric():
            number = int(line[i])
            break
    
    # Finds number from the end of the string
    for i in range(1, size):
        if line[size - i].isnumeric():
            number = number * 10 + int(line[size - i])
            break
    
    if number // 10 == 0:
        number = number * 10 + number
    
    calibration += number

print(calibration)