# --- Part Two ---

# Now moves are not separated for multiple boxes.
# You can move more than one box in a block at the same time (together)

fhandle = open('day5.txt')
matrix = [[],[],[],[],[],[],[],[],[]]
extraction_list = [1,5,9,13,17,21,25,29,33]
for line in fhandle:
    line = line.rstrip()
    if len(line) <= 1:
        pass
    elif (line[1] == '1'):
        pass
    elif (line[0] == '') or (line[0] != 'm'):
        counter = 0
        for i in range(9):
            try:
                if line[extraction_list[counter]] == ' ':
                    pass
                else:
                    matrix[counter].append(line[extraction_list[counter]])
            except:
                pass
            counter += 1

    elif line[0] == 'm':
        line = line.strip()
        line = line.replace(' ', '')
        line = line.replace('move', '')
        line = line.replace('from', '-')
        line = line.replace('to', '-')
        moves = line.split('-')
        print(moves)
        val = matrix[int(moves[1])-1][:int(moves[0])]
        del matrix[int(moves[1])-1][:int(moves[0])]
        for i in range(len(val)):
            matrix[int(moves[2])-1].insert(0,val[-(i+1)])
print(matrix[0][0],matrix[1][0],matrix[2][0],matrix[3][0],matrix[4][0],matrix[5][0],matrix[6][0],matrix[7][0],matrix[8][0])
print(matrix)
