# --- Part Two ---

# How many pair of elves are overlapping the cleaning areas?
# can be entering overlapping or just a part/segment overlapping

# 5-7,7-9
# ....567..  5-7
# ......789  7-9


# xxxxxx
#      xxx
# min2 <= max1 and min2>=min1

#  xxxxx
# xx
# max2 >= Min1  and  max2 <= Max1

#      xxx
# xxxxxx
# min1 >=min2 and min1 <=max2

# xx
#  xxxxx
# max1>=Min2 and max1<=max2


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
    elif (min2 <= max1) and (min2>=min1):
        counter += 1
    elif (max2 >= min1)  and  (max2 <= max1):
        counter += 1
    elif (min1 >=min2) and (min1 <=max2):
        counter += 1
    elif (max1>=min2) and (max1<=max2):
        counter += 1
print(counter)