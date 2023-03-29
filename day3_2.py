# --- Day 3: Rucksack Reorganization --- PART 2

# Each line is one Rucksack.
# Every Rucksack has a badge.
# Every group of 3 Elfs Rucksacks (3 lines), share the same badge.

# Each badge has a value:
# a-z: 1-26
# A-Z: 27-52

# Find the badge that every group shares, and sum the values of all the badges.

#ASCII:
# A=65    (-38)
# Z=90    (-38)
# a=97    (-96)
# b=122   (-96)

fhandle = open("day3_1_rucksack.txt")
group_list = []
group_counter = 0
test_list = []
counter = 0
for line in fhandle:
    line = line.strip()
    print(line)
    group_set = set(line)
    print(group_set)
    for value in group_set:
        group_list.append(value)
    print(group_list)
    group_counter += 1
    print(group_counter)
    if group_counter == 3:
        for x in group_list:
            if group_list.count(x) >2:
                if x.isupper():
                    counter += ord(x)-38
                else:
                    counter += ord(x)-96
                group_counter = 0
                group_list = []
                break
print(counter)


# O(n * m), where n is the number of lines in the file and m is the maximum length of a line.
