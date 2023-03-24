# Elf plays: Rock(A), Paper(B), Scissors(C)
# My play:   Lose(X), Draw(Y), Win(Z)

# Score:
# Win - Your move (Rock) 1, (Paper) 2, (Scissor) 3
# + Outcome of the round = 0 Lost, 3 Draw, 6 Won

# Result of game :
#   Lose Draw Win
#     X   Y   Z
# A   3   1   2
# B   1   2   3
# C   2   3   1

import pandas as pd

df_moves = pd.DataFrame({'X':[3,1,2],
                         'Y':[1,2,3],
                         'Z':[2,3,1]},index=['A','B','C'])

fhandle = open('day2_1_rocksispaper.txt')
total_score = 0
game_result = {'X':0,'Y':3,'Z':6}
for line in fhandle:
        parcial_score = df_moves[line[2]][line[0]] + game_result[line[2]]
        total_score += parcial_score
print(total_score)