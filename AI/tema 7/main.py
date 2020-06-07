
import random
import numpy as np

init_state = (3, 0)
alpha = 0.5
gama = 0.9
n = 4
nr_obstacole = 3
q = [[[0, 0, 0, 0, 0] for i in range(n)] for j in range(n)]


def init_board(n, nr_obs):
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
    if s[0] == n-1 and s[1] == n-1:
        return True
    return False


actions = {"up": 0, "down": 1, "right": 2, "left": 3, "None": 4}


def get_possible_moves(s, board):
    moves = list()
    if s[0] != 0 and board[s[0]-1][s[1]] != -999:
        moves.append(0)
    if s[0] != n-1 and board[s[0]+1][s[1]] != -999:
        moves.append(1)
    if s[1] != 0 and board[s[0]][s[1]-1] != -999:
        moves.append(3)
    if s[1] != n-1 and board[s[0]][s[1]+1] != -999:
        moves.append(2)
    return moves


def go_new_state(s, a):
    if a == 0:
        new_state = (s[0]-1, s[1])
    if a == 1:
        new_state = (s[0]+1, s[1])
    if a == 2:
        new_state = (s[0], s[1]+1)
    if a == 3:
        new_state = (s[0], s[1]-1)
    return new_state

# def Q_Learning_Agent(s, a, r):
#     if is_final(s):
#         q[s[0]][s[1]][4] = r[s[0]][s[1]]
#     else:
#         new_state = go_new_state(s, a)
#         print(s, a)
#         q[s[0]][s[1]][actions[a]] += alpha*(r[s[0]][s[1]] + gama * max(q[new_state[0]][new_state[1]][:]) - q[s[0]][s[1]][actions[a]])
#         print(q)
#         print(max(q[new_state[0]][new_state[1]][:]))
#     s, a = new_state, np.argmax(q[new_state[0]][new_state[1]][:])
#     # return (s, list(actions.keys())[list(actions.values()).index(a)])
#     return (s, a)

def Q_Learning_Agent(s, a, r, s1):
    if is_final(s):
        q[s[0]][s[1]][4] = r
    else:
        # new_state = go_new_state(s, a)
        # print(s, a)
        q[s[0]][s[1]][a] += alpha*(r + gama * max(q[s1[0]][s1[1]][:]) - q[s[0]][s[1]][a])
        # print(q)
        # print(max(q[s1[0]][s1[1]][:]))
    s, a = s1, np.argmax(q[s1[0]][s1[1]][:])
    # return (s, list(actions.keys())[list(actions.values()).index(a)])
    return (s, a)

def training(board):
    s = init_state
    drum = list()
    moves = get_possible_moves(s, board)
    x = random.randint(0, len(moves) - 1)
    new_state = go_new_state(s, moves[x])
    rez = Q_Learning_Agent(s, moves[x], board[s[0]][s[1]], new_state)
    s = rez[0]
    a = rez[1]
    drum.append(moves[x])

    while not is_final(s):
        # print(s)
        moves = get_possible_moves(s, board)
        if max(q[s[0]][s[1]][:]) == min(q[s[0]][s[1]][:]):
            x = random.randint(0, len(moves) - 1)
        else:
            x = np.argmax(q[s[0]][s[1]][:])
        rez = Q_Learning_Agent(s, a, board[s[0]][s[1]], moves[x])
        s = rez[0]
        a = rez[1]
        drum.append(moves[x])
    return drum


board = [[-0.04, -0.04, -0.04, -0.04],
         [-0.04, -0.04, -0.04, -1],
         [-0.04, -999, -0.04, -0.04],
         [-0.04, -0.04, -0.04, 1]]
if __name__ == "__main__":

    my_board = init_board(n, 1)
    print_board(my_board)
    print(training(my_board))
    # print(Q_Learning_Agent((1, 0), "down", board))