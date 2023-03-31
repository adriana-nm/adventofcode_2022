# --- Day 5: Supply Stacks ---

# You will have an input matrix with letter in columns.
# Below there will be instructions.
# You need to move the amount of letters indicated in the instructions from & to the column indicated.
# You only one box at a time and it's always the box that's on top of the column.

#     [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2


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
        for j in range(int(moves[0])):
            val = matrix[int(moves[1])-1].pop(0)
            matrix[int(moves[2])-1].insert(0,val)
print(matrix[0][0],matrix[1][0],matrix[2][0],matrix[3][0],matrix[4][0],matrix[5][0],matrix[6][0],matrix[7][0],matrix[8][0])
print(matrix)






