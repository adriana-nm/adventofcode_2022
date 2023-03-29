# --- Day 3: Rucksack Reorganization --- PART 1

# Each line is one Rucksack. Each rucksack has 2 compartments of equal size.
# There's an item repeated in both compartments.

# Each item has a value:}
# a-z: 1-26
# A-Z: 27-52

# Find the duplicated items and sum the value of all these items

#ASCII:
# A=65    (-38)
# Z=90    (-38)
# a=97    (-96)
# b=122   (-96)


fhandle = open('day3_1_rucksack.txt')
counter = 0
for line in fhandle:
    compartment_length = len(line.strip())/2
    length = 0
    temp_list = []
    for value in line.strip():
        if length >= compartment_length:
            if value in temp_list:
                if value.isupper():
                    counter += ord(value)-38
                else:
                    counter += ord(value)-96
                break
        else:
            length += 1
            temp_list.append(value)
print(counter)

#Big O Notation: O(n*k)