
import math
n = int(input("Number : "))

valori_posibile = [[i for i in range(0, n)] for j in range(0, n)]
valori_de_sters = list()
print(valori_posibile)

def delete_from_values():
    for column in range(0,len(valori_posibile)):
        #valori = list()
        flag = 0
        for column2 in range(0, len(valori_posibile)):
            if column2 != column:
                for el in range(0,len(valori_posibile[column])):
                    for el2 in range(0, len(valori_posibile[column2])):
                        #print(valori_posibile[column][el], valori_posibile[column2][el2])
                        print('1  '+str(abs(valori_posibile[column][el] - valori_posibile[column2][el2])))
                        print('2  ' + str(abs(column - column2)))
                        if valori_posibile[column][el] != valori_posibile[column2][el2] and abs(
                                valori_posibile[column][el] - valori_posibile[column2][el2]) != abs(column - column2):
                            #print(valori_posibile[column][el], valori_posibile[column2][el2] )
                            print('aici')
                            flag = 1
        if flag == 0:
            valori_de_sters.append((column, el))
    print(valori_de_sters)
    # for el in valori_de_sters:
    #     del valori_posibile[el[0]][el[1]]



'''


M = [[0 for i in range(n)] for j in range(n)]
 

def valid_piece(mat, x, y):
    for i in range(n):
        if mat[i][y] == 1 and i != x:
            return False
    i, j = x - 1, y - 1
    while 0 <= i < n and 0 <= j < n:
        if mat[i][j] == 1:
            return False
        i = i - 1
        j = j - 1
    i, j = x - 1, y + 1
    while 0 <= i < n and 0 <= j < n:
        if mat[i][j] == 1:
            return False
        i = i - 1
        j = j + 1
    return True



def bktr(mat, line):

    if line == n:
        return True

    l = list()
    for i in range(n):
        if valid_piece(mat, line, i):
            l.append(i)
    print(l, line)
    for i in l:
        mat[line][i] = 1
        if bktr(mat, line + 1):
            return True
        else:
            mat[line][i] = 0

    return False
'''

l = list()


def valid_piece(x):
    for i in range(len(l)):
        if l[i] == x:
            return False
        if l[i] + (len(l) - i) == x:
            return False
        if l[i] - (len(l) - i) == x:
            return False
    return True


def bktr():
    if len(l) == n:
        return True

    ## Forword chacking for
    possible_assignations = list()
    for i in range(n):
        if valid_piece(i):
            possible_assignations.append(i)
    for i in possible_assignations:
        l.append(i)
        if bktr():
            return True
        else:
            l.pop()

    return False



if __name__ == "__main__":
    delete_from_values()
    print(bktr())
    print(l)
    print(valori_posibile)