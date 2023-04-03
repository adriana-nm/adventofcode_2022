# --- Part Two ---

# Instead of 4 characters it is 14 characters

fhandle = open('day6.txt')
line = fhandle.readline()
l = []
for i in range(len(line)):
    s = set([line[i],line[i+1],line[i+2],line[i+3],line[i+4],line[i+5],line[i+6],line[i+7],line[i+8],line[i+9],
             line[i+10],line[i+11],line[i+12],line[i+13]])
    if len(s) == 14:
        print(i+14)
        break