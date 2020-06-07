
eps = pow(10, -10)

def read_sparse_matrix(path):
    f = open(path, "r+")
    n = int(f.readline())
    valori = [list() for _ in range(n)]
    ind_col = [list() for _ in range(n)]

    for content in f.readlines()[:-1]:
        content = content.rstrip().split(',')
        x = int(content[1])
        y = int(content[2])
        if y not in ind_col[x]:
            valori[x].append(float(content[0]))
            ind_col[x].append(y)
        else:
            valori[x][ind_col[x].index(y)] += float(content[0])

    return valori, ind_col

def completematrix(valori, ind_col):
    max_row = max([len(x) for x in ind_col])
    for i in range(len(valori)):
        while len(valori[i]) < max_row:
            valori[i].append(-1)

    for i in range(len(ind_col)):
        while len(ind_col[i]) < max_row:
            ind_col[i].append(-1)


def read_b(path):
    f = open(path, "r+")
    res = list()

    for content in f.readlines()[1:-1]:
        res.append(float(content))

    return res

def checkDiagonala(indice_col):
    for row in range(len(indice_col)):
        if row not in indice_col[row]:
            return False
    return True

def calc_xc_v2(valori, indice_col, b, xc):
    delta_x = 0

    for row in range(len(indice_col)):
        aii = valori[row][indice_col[row].index(row)]
        suma = b[row]
        for i in range(len(valori[row])):
            if indice_col[row][i] != row and indice_col[row][i] != -1:
                suma -= valori[row][i] * xc[indice_col[row][i]]

        new_x = suma / aii
        delta_x += abs(xc[row] - new_x)
        xc[row] = new_x

    return xc, delta_x


def tema4(path_a, path_b):
    k_max = 10000
    valori, indice_col = read_sparse_matrix(path_a)
    if checkDiagonala(indice_col):
        xc = [0 for _ in range(len(indice_col))]
        b = read_b(path_b)

        k = 0
        while True:

            xc, delta_x = calc_xc_v2(valori, indice_col, b, xc)

            k += 1

            if k > k_max or delta_x < eps or delta_x > pow(10, 9):
                break

        if delta_x < eps:

            Axgs_b = list()
            for row in range(len(indice_col)):
                sum = 0
                for i in range(len(indice_col[row])):
                    if indice_col[row][i] != -1:
                        sum += valori[row][i] * xc[indice_col[row][i]]
                Axgs_b.append(abs(sum - b[row]))

            norma = max(Axgs_b)
            return norma, xc
        else:
            return "Divergent"
    else:
        return "Nu se poate rezolva"

def get_res(case):
    path_a = 'a_' + case + '.txt'
    path_b = 'b_' + case + '.txt'
    res = tema4(path_a, path_b)
    return res


import os
def citire(d):
    file1 = open('a.txt', 'r')
    line = file1.readline()
    d = {}
    for i in (0, line):
        d[i] = {}
    count = 1
    print(d)
    while True:
        count += 1
        # Get next line from file
        line = file1.readline()
        x = line.split(" ,")
        if x[2] in d[x[1]]:
            d[x[1]][x[2]] = d[x[1]][x[2]] + x[0]
        else:
            d[x[1]][x[2]] = x[0]
        # if line is empty
        # end of file is reached
        if not line:
            break
    for i in (1, line):
        if len(d[i] > 10):
            print("Prea multe elemente")
            break
def adunare(a,b):
    c = {}
    for i in (0,2019):
        for j in (0,2019):
            if j in a[i] and j in b[i]:
                c[i][j] = a[i][j] + b[i][j]
            elif (j in a[i] and j not in b[i]):
                c[i][j] = a[i][j]
            elif (j in b[i] and j not in a[i]):
                c[i][j] = b[i][j]
    for i in (1, 2019):
        if len(c[i] > 10):
            print("Prea multe elemente")
            break
if __name__ == "__main__":
    citire(0)