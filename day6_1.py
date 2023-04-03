# --- Day 6: Tuning Trouble ---

# You have a code that has a four character marker
# The marker are all different letters
# Once you find the marker you need to know how many characters have been read in that line
# ( list position + 1)

# mjqjpqmgbljsphdztnvjfqwrcgsmlb
# marker: jpqm
# position of last value: 7


fhandle = open('day6.txt')
line = fhandle.readline()
l = []
for i in range(len(line)):
    s = set([line[i],line[i+1],line[i+2],line[i+3]])
    if len(s) == 4:
        print(i+4)
        break



