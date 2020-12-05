import math as m

table = [1,2,3,4]
total_steps = sum(table)

def Stop_game(matrix):
    for i in matrix:
        if i > 0:
            return False
    return True

def Player():
    index = int(input("Index of stack: "))
    index = min(max(0, index), len(table)-1)
    while table[index] <= 0:
        index = int(input("Index of stack: "))
        index = min(max(0, index), len(table)-1)
    value = int(input("Number of items: "))
    value = min(max(1, value), table[index])
    table[index] -= value

def min_max(isMax, steps, alpha, beta):
    if Stop_game(table):
        raw_value = total_steps - steps
        if isMax:
            return raw_value
        else:
            return -raw_value
    if isMax:
        best_score = -m.inf
        for i in range(len(table)):
            if table[i] > 0:
                for j in range(1, table[i]+1):
                    table[i] -= j
                    score = min_max(False, steps+1, alpha, beta)
                    table[i] += j
                    best_score = max(score, best_score)
                    alpha = max(alpha, score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = m.inf
        for i in range(len(table)):
            if table[i] > 0:
                for j in range(1, table[i]+1):
                    table[i] -= j
                    score = min_max(True, steps+1, alpha, beta)
                    table[i] += j
                    best_score = min(score, best_score)
                    beta = min(beta, score)
                    if beta <= alpha:
                        break
        return best_score


def AI():
    best_score = -m.inf
    move = ()
    for i in range(len(table)):
        if table[i] > 0:
            for j in range(1, table[i]+1):
                print("trying move " + str(i) + " " + str(j))
                table[i] -= j
                score = min_max(False, 0, -m.inf, m.inf)
                table[i] += j
                if score > best_score:
                    best_score = score
                    move = (i, j)
    table[move[0]] -= move[1]
    print("The AI has removed " +str(move[1]) + " items from stock number " + str(move[0]))

def Game():
    player_move = True
    while Stop_game(table) == False:
        print(table)
        if player_move:
            print("Player move:")
            Player()
        else:
            print("AI move:")
            AI()
        player_move = not player_move
    if player_move:
        print("The player has won")
    else:
        print("The AI has won")


Game()
'''
print(table)
print(Stop_game())
'''

'''
NOTES:
using minmax()
the AI will try its best to play as the max player
while the real human has the intent of a min player
max == "getting to the end as quick as possible"
min == "picking nodes that lead to AI's loss"

ways of calculating the minmax value:
    raw_value = total_possible_steps - step_number
    if AI wins:
        final_value = +raw_value
    else:
        final_value = -raw_value
Min player will try to get the min(final_value)
Max player will try to get the max(final_value)
'''
