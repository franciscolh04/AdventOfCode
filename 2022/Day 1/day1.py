calories, maxCalories, secondCalories, thirdCalories = 0, 0, 0, 0

with open("2022/day1.in", "r") as file:
    lines = [line.strip() for line in file.readlines()]

for line in lines:
    if (len(line) != 0):
        calories += int(line)
    else:
        if calories > maxCalories:
            thirdCalories = secondCalories
            secondCalories = maxCalories
            maxCalories = calories
        elif calories > secondCalories:
            thirdCalories = secondCalories
            secondCalories = calories
        elif calories > thirdCalories:
            thirdCalories = calories
        calories = 0

print("Max calories: " + str(maxCalories))
print("Second max calories: " + str(secondCalories))
print("Third max calories: " + str(thirdCalories) + "\n")
print("Total: " + str(maxCalories + secondCalories + thirdCalories))