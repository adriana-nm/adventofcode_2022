#Day 1: Calorie Counting

# The Elves take turns writing down the number of Calories contained by the various meals, snacks, rations, etc. that
# they've brought with them, one item per line. Each Elf separates their own inventory from the previous Elf's
# inventory (if any) by a blank line.

# Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?


fhandle = open('day1_1_calories.txt')
total_calories = []
elf_tot_cal = 0
for line in fhandle:
    if len(line.strip()) == 0:
        total_calories.append(elf_tot_cal)
        elf_tot_cal = 0
    else:
        line = line.strip()
        elf_tot_cal += int(line)
print(max(total_calories))
