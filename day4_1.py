# --- Day 4: Camp Cleanup ---

# Each pair of elf has been assigned an area of cleaning
# Ex. 23-33,24-65
# If one area of cleaning is completely inside the other one (or vice-versa) then both elves would be
# cleaning the same area.

# Ex. 2-8,3-7
#.2345678.  2-8
#..34567..  3-7

# Count how many times this is happening.


fhandle = open('day4.txt')
counter = 0
for line in fhandle:
    line = line.strip()
    line = line.split(',')
    line0 = line[0].split('-')
    line1 = line[1].split('-')
    min1 = int(line0[0])
    max1 = int(line0[1])
    min2 = int(line1[0])
    max2 = int(line1[1])
    if (min2 >= min1) and (max2 <= max1):
        counter += 1
    elif (min1 >= min2) and (max1 <= max2):
        counter += 1
print(counter)