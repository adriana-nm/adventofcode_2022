# --- Part Two ---

# How many calories in total have the top 3 elves with most calories?

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
total_calories.sort(reverse=True)
sum_cal = total_calories[0] + total_calories[1] + total_calories[2]
print(sum_cal)
