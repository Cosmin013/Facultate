import copy
'''
#                 0   1  2  3  4  5  6  7
board_initial = [[0, 1, 0, 1, 0, 1, 0, 1],  # 0
                 [1, 0, 1, 0, 1, 0, 1, 0],  # 1
                 [0, 1, 0, 1, 0, 1, 0, 1],  # 2
                 [0, 0, 0, 0, 0, 0, 0, 0],  # 3
                 [0, 0, 0, 0, 0, 0, 0, 0],  # 4
                 [2, 0, 2, 0, 2, 0, 2, 0],  # 5
                 [0, 2, 0, 2, 0, 2, 0, 2],  # 6
                 [2, 0, 2, 0, 2, 0, 2, 0]]  # 7

'''
board_initial = [[0, 1, 0, 1, 0, 1, 0, 1],  # 0
                 [1, 0, 1, 0, 1, 0, 1, 0],  # 1
                 [0, 1, 0, 1, 0, 1, 0, 1],  # 2
                 [0, 0, 2, 0, 1, 0, 0, 0],  # 3
                 [0, 0, 0, 0, 0, 2, 0, 0],  # 4
                 [2, 0, 2, 0, 0, 0, 0, 0],  # 5
                 [0, 2, 0, 2, 0, 2, 0, 2],  # 6
                 [2, 0, 2, 0, 0., 0, 2, 0]]  # 7


# the game is over and one player wins when the other player runs out of pieces on the board
# or when he has no possible moves
def is_final(m, player):
    if player == 1:  # pc
        for i in range(8):
            for j in range(8):
                if m[i][j] == 1 or m[i][j] == 3:
                    if not possible_moves_human(m):
                        return True
    elif player == 2:  # human
        for i in range(8):
            for j in range(8):
                if m[i][j] == 2 or m[i][j] == 4:
                    if not possible_moves_pc(m):
                        return True
    return False


def possible_moves_pc(m):
    moves = list()
    for i in range(8):
        for j in range(8):
            if m[i][j] == 1 or m[i][j] == 3:
                if i + 1 < 8:
                    if j + 1 < 8 and m[i + 1][j + 1] == 0:
                        moves.append([(i, j), (i + 1, j + 1)])
                    if j - 1 >= 0 and m[i + 1][j - 1] == 0:
                        moves.append([(i, j), (i + 1, j - 1)])
                if i + 2 < 8:
                    if j + 2 < 8 and (m[i + 1][j + 1] == 2 or m[i + 1][j + 1] == 4) and m[i + 2][j + 2] == 0:
                        moves.append([(i, j), (i + 2, j + 2)])
                    if j - 2 >= 0 and (m[i + 1][j - 1] == 2 or m[i + 1][j - 1] == 4) and m[i + 2][j - 2] == 0:
                        moves.append([(i, j), (i + 2, j - 2)])

            if m[i][j] == 3:
                if i - 1 >= 0:
                    if j + 1 < 8 and m[i - 1][j + 1] == 0:
                        moves.append([(i, j), (i - 1, j + 1)])
                    if j - 1 >= 0 and m[i - 1][j - 1] == 0:
                        moves.append([(i, j), (i - 1, j - 1)])

                if i - 2 >= 0:
                    if j + 2 < 8 and (m[i - 1][j + 1] == 2 or m[i - 1][j + 1] == 4) and m[i - 2][j + 2] == 0:
                        moves.append([(i, j), (i - 2, j + 2)])
                    if j - 2 >= 0 and (m[i - 1][j - 1] == 2 or m[i - 1][j - 1] == 4) and m[i - 2][j - 2] == 0:
                        moves.append([(i, j), (i - 2, j - 2)])
    return moves


def possible_moves_human(m):
    moves = list()
    for i in range(8):
        for j in range(8):
            if m[i][j] == 2 or m[i][j] == 4:
                if i - 1 >= 0:
                    if j + 1 < 8 and m[i - 1][j + 1] == 0:
                        moves.append([(i, j), (i - 1, j + 1)])
                    if j - 1 >= 0 and m[i - 1][j - 1] == 0:
                        moves.append([(i, j), (i - 1, j - 1)])

                if i - 2 >= 0:
                    if j + 2 < 8 and (m[i - 1][j + 1] == 1 or m[i - 1][j + 1] == 3) and m[i - 2][j + 2] == 0:
                        moves.append([(i, j), (i - 2, j + 2)])
                    if j - 2 >= 0 and (m[i - 1][j - 1] == 1 or m[i - 1][j - 1] == 3) and m[i - 2][j - 2] == 0:
                        moves.append([(i, j), (i - 2, j - 2)])

            if m[i][j] == 4:
                if i + 1 < 8:
                    if j + 1 < 8 and m[i + 1][j + 1] == 0:
                        moves.append([(i, j), (i + 1, j + 1)])
                    if j - 1 >= 0 and m[i + 1][j - 1] == 0:
                        moves.append([(i, j), (i + 1, j - 1)])

                if i + 2 < 8:
                    if j + 2 < 8 and (m[i + 1][j + 1] == 1 or m[i + 1][j + 1] == 3) and m[i + 2][j + 2] == 0:
                        moves.append([(i, j), (i + 2, j + 2)])
                    if j - 2 >= 0 and (m[i + 1][j - 1] == 1 or m[i + 1][j - 1] == 3) and m[i + 2][j - 2] == 0:
                        moves.append([(i, j), (i + 2, j - 2)])
    return moves


def make_move(board, move):
    m = copy.deepcopy(board)

    eat = False
    if abs(move[1][0] - move[0][0]) == 1:  # make one step in any direction
        m[move[1][0]][move[1][1]] = m[move[0][0]][move[0][1]]
    if move[1][0] - move[0][0] == 2:  # make 2 steps in front
        if move[1][1] - move[0][1] > 0:  # make 2 step right
            m[move[0][0] + 1][move[0][1] + 1] = 0
            m[move[1][0]][move[1][1]] = m[move[0][0]][move[0][1]]
            eat = True
        else:  # make 2 step left
            m[move[0][0] + 1][move[0][1] - 1] = 0
            m[move[1][0]][move[1][1]] = m[move[0][0]][move[0][1]]
            eat = True
    elif move[1][0] - move[0][0] == -2:  # make 2 steps back
        if move[1][1] - move[0][1] > 0:  # make 2 steps right
            m[move[0][0] - 1][move[0][1] + 1] = 0
            m[move[1][0]][move[1][1]] = m[move[0][0]][move[0][1]]
            eat = True
        else:  # make 2 steps left
            m[move[0][0] - 1][move[0][1] - 1] = 0
            m[move[1][0]][move[1][1]] = m[move[0][0]][move[0][1]]
            eat = True
    m[move[0][0]][move[0][1]] = 0

    if eat:
        for i in possible_moves_pc(m):
            if i[0] == move[1]:
                if abs(i[1][0] - i[0][0]) == 2:
                    return make_move(m, i)
        for i in possible_moves_human(m):
            if i[0] == move[1]:
                if abs(i[1][0] - i[0][0]) == 2:
                    return make_move(m, i)

    return m


# the number of remaining pieces of the human
def h(m):
    score = 0
    count = 0
    for i in range(8):
        for j in range(8):
            if m[i][j] == 2:
                score = score - ((i+1) // 2)
                count += 1

    score = score - (count * 7)

    for i in range(8):
        for j in range(8):
            if m[i][j] == 1:
                score = score - ((8 - i) // 2)
                count += 1

    score = score + count * 7

    for i in range(8):
        for j in range(8):
            if m[i][j] == 4:
                count += 1

    score = score - count * 10

    for i in range(8):
        for j in range(8):
            if m[i][j] == 3:
                count += 1

    score = score + count * 10

    score = score + len(possible_moves_pc(m))

    score = score - len(possible_moves_human(m))

    return score


def minimax(m):
    pc_moves = possible_moves_pc(m)
    score_move = list()
    alpha = 0
    for i in pc_moves:
        new_board = make_move(m, i)
        human_moves = possible_moves_human(new_board)
        scores = list()
        for j in human_moves:
            scor = h(make_move(new_board, j))
            scores.append((scor, i))
            if scor < alpha:
                break

        scores.sort(key=lambda a: a[0])
        score_move.append(scores[0])
        if alpha > scores[0][0]:
            alpha = scores[0][0]

    score_move.sort(key=lambda a: a[0], reverse=True)
    return score_move[0]


# pc calculates the heuristic for each possible move and chooses to make the one with the minimum value
def best_pc_move(m):
    pc_moves = possible_moves_pc(m)
    score_move = list()
    for i in pc_moves:
        score_move.append((h(make_move(m, i)), i))

    score_move.sort(key=lambda j: j[0], reverse=True)
    return score_move[0]


# when the player reaches the end of the board with a piece,
# he can move the respective piece back and forth during the game
def update_board(m):
    for i in range(8):
        if m[7][i] == 1:
            m[7][i] = 3
        if m[0][i] == 2:
            m[0][i] = 4
    return m


def print_board(m):
    print(' 0, 1, 2, 3, 4, 5, 6, 7')
    for i in range(8):
        print(m[i], i)


def start_game(board):
    m = board
    print('Initial state/Start game:')
    print_board(board_initial)
    while not (is_final(m, 1) and is_final(m, 2)):
        pc_move = minimax(m)[1]  # pc start the game
        m = make_move(m, pc_move)  # pc make move
        update_board(m)  # update board if its necessary
        print('Pc make the move: ', pc_move)
        print_board(m)

        # input ij xy, where ij is the piece you want to move and xy is the position where you move it
        if not is_final(m, 1):
            human_move = input("Enter your move: ")
            human_move = [(int(human_move[0]), int(human_move[1])), (int(human_move[3]), int(human_move[4]))]
            if human_move in possible_moves_human(m):
                m = make_move(m, human_move)
                update_board(m)
                print_board(m)
            else:
                while human_move not in possible_moves_human(m):
                    human_move = input("Your move is illegal, try another one: ")
                    human_move = [(int(human_move[0]), int(human_move[1])), (int(human_move[3]), int(human_move[4]))]
                else:
                    m = make_move(m, human_move)
                    update_board(m)
                    print_board(m)
        else:
            print('Pc win the game!')
            break
    else:
        print('You win the game! Congrats!')


if __name__ == "__main__":
    start_game(board_initial)
