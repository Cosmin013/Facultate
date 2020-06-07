


l = list()

def bktr(possible_moves, depth):
    if len(l) == n:
        return True

    for i in possible_moves[len(l)]:
        ps_copy = possible_moves.copy()

        if update_forward(ps_copy):
            return False

        if bktr(ps_copy):
            return True
        else:
            l.pop()

    return False


def update_forward(possible_moves):
    for i in range(len(l)+1, )


    abs( valori_posibile[column][el] - valori_posibile[column2][el2] ) != abs(column - column2):



if __name__ == "__main__" :
    n = int(input("Number : "))
    possible_moves = [[i for i in range(n)] for i in range(n)]
    bktr(possible_moves)


