
eps = pow(10, -10)

def read_sparse_matrix(path):

    f = open(path, "r+")
    n = int(f.readline())
    res = [list() for _ in range(n)]


    for content in f.readlines()[:-1]:
        content = content.rstrip().split(',')
        new_element = [float(content[0]), int(content[2])]
        row = int(content[1])
        found = -1
        for i in range(len(res[row])):
            if res[row][i][1] == new_element[1]:
                found = i
                break
        if found != -1:
            res[row][found][0] += new_element[0]
        else:
            res[row].append(new_element)

    for i in range(len(res)):
        res[i].sort(key=lambda x: x[1])


    return res, n


def read_b(path):
    f = open(path, "r+")
    res = list()

    for content in f.readlines()[1:-1]:
        res.append(float(content))

    return res


def checkDiagonala(A, n):
    for row in range(len(A)):
        found = False
        for element in A[row]:
            if element[1] == row and abs(element[0]) > eps:
                found = True
                break
        if found == False:
            return False
    return True


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


def calc_xc(A, b, xp):
    xc = list()
    delta_x = 0
    for row in range(len(A)):
        aii = 0
        sum = b[row]
        for element in A[row]:
            if element[1] == row:
                aii = element[0]
            else:
                sum -= element[0] * xp[element[1]]

        xc.append(sum / aii)
        delta_x += abs(xp[row] - xc[row])
    return xc, delta_x


def calc_xc_v2(A, b, xc):
    delta_x = 0

    for row in range(len(A)):
        aii = 0
        sum = b[row]
        for element in A[row]:
            if element[1] == row:
                aii = element[0]
            else:
                sum -= element[0] * xc[element[1]]

        new_x = sum / aii
        delta_x += abs(xc[row] - new_x)
        xc[row] = new_x
    return xc, delta_x


def tema4(path_a, path_b):
    k_max = 10000
    A, n = read_sparse_matrix(path_a)
    if checkDiagonala(A, n):
        xc = [0 for _ in range(n)]
        b = read_b(path_b)

        k = 0
        while True:

            xc, delta_x = calc_xc(A, b, xc)

            k += 1

            if k > k_max or delta_x < eps or delta_x > pow(10, 9):
                break

        if delta_x < eps:

            Axgs_b = list()
            for row in range(len(A)):
                sum = 0
                for element in A[row]:
                    sum += element[0] * xc[element[1]]
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
