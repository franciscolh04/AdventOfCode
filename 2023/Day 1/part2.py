calibration = 0
number = 0

numbers = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

# Read input
with open("2023/Day 1/day1.in", "r") as file:
    lines = [line.strip() for line in file.readlines()]

for line in lines:
    size = len(line)
    first, second = 0, 0

    # Finds number from the beginning of the line
    for i in range(size):
        if line[i].isnumeric():
            first = int(line[i])
            break
    
    # Finds written number from the beggining of the line
    exist = {}
    for i in numbers:
        if i in line:
            exist[i] = line.find(i)
    
    if len(exist) != 0:
        firstWritten = min(exist, key=exist.get)
        if first == 0 or line.find(str(first)) > line.find(firstWritten):
            first = numbers[firstWritten]
    
    # Finds number from the end of the line
    for i in range(1, size):
        if line[size - i].isnumeric():
            second = int(line[size - i])
            break
    
    # Finds written number from the end of the line
    exist = {}
    for i in numbers:
        if i in line:
            exist[i] = line.rfind(i)
    
    if len(exist) != 0:
        secondWritten = max(exist, key=exist.get)
        if second == 0 or line.rfind(str(second)) < line.rfind(secondWritten):
            second = numbers[secondWritten]

    # Special cases
    if size == 1:
        number = int(line + line)
    elif first == 0:
        number = second * 10 + second
    elif second == 0:
        number = first * 10 + first
    else:
        number = first * 10 + second
    
    calibration += number

print(calibration)