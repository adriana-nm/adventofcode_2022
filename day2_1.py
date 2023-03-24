# --- Day 2: Rock Paper Scissors ---

# Elf plays: Rock(A), Paper(B), Scissors(C)
# My play:   Rock(X), Paper(Y), Scissors(Z)
# R > S, S>P, P> R

# Score:
# Win - Your move (X) 1, (Y) 2, (Z) 3
# + Outcome of the round = 0 Lost, 3 Draw, 6 Won

# Result of game :
#     X   Y   Z
# A   3   6   0
# B   0   3   6
# C   6   0   3

import pandas as pd

df_moves = pd.DataFrame({'X':[3,0,6],
                         'Y':[6,3,0],
                         'Z':[0,6,3]},index=['A','B','C'])

fhandle = open('day2_1_rocksispaper.txt')
total_score = 0
my_move = {'X':1,'Y':2,'Z':3}
for line in fhandle:
        parcial_score = df_moves[line[2]][line[0]] + my_move[line[2]]
        total_score += parcial_score
print(total_score)
