

import random
import numpy as np

alpha = 0.5
gama = 0.9
n = 10

init_state = (0, 0)
final_state = (n-1, n-1)

nr_obs = 30
q = [[[0, 0, 0, 0] for i in range(n)] for j in range(n)]


def init_rewords():
    board = [[-0.04 for i in range(n)] for j in range(n)]
    cordonates = list()

    for i in range(nr_obs):
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        while (x, y) in cordonates or (x == n-1 and y == n-1) or (x == init_state[0] and y == init_state[1]) :
            x = random.randint(0, n-1)
            y = random.randint(0, n-1)
        else:
            cordonates.append((x, y))

    for obstacle in cordonates:
        board[obstacle[0]][obstacle[1]] = -999

    board[n-1][n-1] = 1

    obstacle_x = random.randint(0 , n-1)
    obstacle_y = random.randint(0, n - 1)

    while (obstacle_x, obstacle_y) in cordonates or (obstacle_y == n-1 and obstacle_x == n-1) or (obstacle_y == init_state[1] and obstacle_x == init_state[0]):
        obstacle_x = random.randint(0, n - 1)
        obstacle_y = random.randint(0, n - 1)
    board[obstacle_x][obstacle_y] = -1

    return board


def print_board(board):
    for row in board:
        print(row)


def is_final(s):
    if s == final_state:
        return True
    return False


def go_new_state(s, a, board):
    if a == 0 and (s[0] == 0 or board[s[0]-1][s[1]] == -999):
        return s
    if a == 1 and (s[0] == n-1 or board[s[0]+1][s[1]] == -999):
        return s
    if a == 3 and (s[1] == 0 or board[s[0]][s[1]-1] == -999):
        return s
    if a == 2 and (s[1] == n-1 or board[s[0]][s[1]+1] == -999):
        return s

    if a == 0:
        return (s[0]-1, s[1])
    if a == 1:
        return (s[0]+1, s[1])
    if a == 2:
        return (s[0], s[1]+1)
    if a == 3:
        return (s[0], s[1]-1)



def Q_Learning_Agent(s, a, r):

    if is_final(s):
        q[s[0]][s[1]][4] = r[s[0]][s[1]]
    else:
        new_state = go_new_state(s, a)
        print(s, a)
        q[s[0]][s[1]][actions[a]] += alpha*(r[s[0]][s[1]] + gama * max(q[new_state[0]][new_state[1]][:]) - q[s[0]][s[1]][actions[a]])
        print(q)
        print(max(q[new_state[0]][new_state[1]][:]))
    s, a = new_state, np.argmax(q[new_state[0]][new_state[1]][:])
    # return (s, list(actions.keys())[list(actions.values()).index(a)])
    return (s, a)


def training(s, r):
    drum = list()
    counter = 0
    while True:
        if max(q[s[0]][s[1]][:]) == min(q[s[0]][s[1]][:]):
            x = random.randint(0, 3)
        else:
            x = np.argmax(q[s[0]][s[1]][:])
            if q[s[0]][s[1]].count(q[s[0]][s[1]][x]) > 1:
                l = list()
                for i in range(3):
                    if q[s[0]][s[1]][i] == q[s[0]][s[1]][x]:
                        l.append(i)
                j = random.randint(0, len(l) - 1 )
                x = l[j]


        new_state = go_new_state(s, x, r)
        q[s[0]][s[1]][x] += alpha * (r[s[0]][s[1]] + gama * max(q[new_state[0]][new_state[1]][:]) - q[s[0]][s[1]][x])
        s = new_state
        drum.append(x)
        if is_final(s):
            s = init_state
            counter += 1
            if counter == 1000:
                return drum
            else:
                print(drum)
                drum = list()


actions = { 0 :"up", 1:"down", 2:"right", 3:"left"}

board = [[-0.04, -0.04, -0.04, -0.04],
         [-0.04, -0.04, -0.04, -1],
         [-0.04, -999, -0.04, -0.04],
         [-0.04, -0.04, -0.04, 1]]


if __name__ == "__main__":
    my_board = init_rewords()
    print_board(my_board)
    x = training(init_state, my_board)
    # print(x)
    tradus = list()
    for i in x:
        tradus.append(actions[i])
    print(tradus)