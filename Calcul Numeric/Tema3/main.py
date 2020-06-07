
def read_sparse_matrix(path, max_per_line):

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
        if len(res[i]) > max_per_line:
            print("From file " + path + " more then " + str(max_per_line) + ', ' + str(len(res[i])) + " elements on line " + str(i))

    for i in range(len(res)):
        res[i].sort(key=lambda x: x[1])


    return res, n


def add(A, n_a, B, n_b):

    if n_a != n_b:
        print("Matrices can't be added")
        return 0
    else:
        res = [list() for _ in range(n_b)]
        row = 0
        while row < len(A):
            a, b = 0, 0
            while a < len(A[row]) and b < len(B[row]):
                if A[row][a][1] > B[row][b][1]:
                    res[row].append(B[row][b])
                    b += 1
                elif A[row][a][1] < B[row][b][1]:
                    res[row].append(A[row][a])
                    a += 1
                else:
                    new_element = [A[row][a][0]+B[row][b][0], A[row][a][1]]
                    res[row].append(new_element)
                    a += 1
                    b += 1
            while a < len(A[row]):
                res[row].append(A[row][a])
                a += 1
            while b < len(B[row]):
                res[row].append(B[row][b])
                b += 1
            row += 1

    return res

def transpusa(M):
    res = [list() for _ in range(len(M))]

    for row in range(len(M)):
        for element in range(len(M[row])):
            res[M[row][element][1]].append([M[row][element][0], row])

    for i in range(len(res)):
        res[i].sort(key=lambda x: x[1])

    return res



def multiply(A, B):
    B = transpusa(B)
    res = [list() for _ in range(len(A))]

    for row in range(len(A)):
        for col in range(len(A)):
            a, b = 0, 0
            sum = 0
            while a < len(A[row]) and b < len(B[col]):
                if A[row][a][1] > B[col][b][1]:
                    b += 1
                elif A[row][a][1] < B[col][b][1]:
                    a += 1
                else:
                    sum += A[row][a][0] * B[col][b][0]
                    a += 1
                    b += 1
            if sum != 0:
                res[row].append([sum, col])

    return res

def equals(A, B):
    epsilon = 0.00001

    for i in range(len(A)):
        A[i].sort(key=lambda x: x[1])

    for i in range(len(B)):
        B[i].sort(key=lambda x: x[1])

    if len(A) != len(B):
        return False

    for row in range(len(A)):
        if len(A[row]) != len(B[row]):
            return False
        for element in range(len(A[row])):
            if A[row][element][1] == B[row][element][1]:
                if abs(A[row][element][0] - B[row][element][0]) > epsilon:
                    return False
            else:
                return False
    return True


def write_to(A , path):
    f = open(path, "w")
    f.write('{')
    for i in A:
        f.write(str(i).replace('[', '{').replace(']', '}') + '\n')
    f.write('}')
    f.close()


def calc(path1, path2, rezori, rezplus, saveplus, saveori):

    A, n_A = read_sparse_matrix(path1, 11)
    B, n_B = read_sparse_matrix(path2, 11)


    AplusB, n_AplusB = read_sparse_matrix(rezplus, 22)

    myAplusB = add(A, n_A, B, n_B)

    AoriB, n_AoriB = read_sparse_matrix(rezori, 90000)

    A, n_A = read_sparse_matrix(path1, 11)
    B, n_B = read_sparse_matrix(path2, 11)

    myAoriB = multiply(A, B)

    write_to(myAplusB, saveplus)
    write_to(myAoriB, saveori)


    if equals(myAplusB, AplusB) and str(myAplusB) == str(AplusB):
        rez = 'Adunare corecta \n'
    else:
        rez = 'Adunare gresita \n'

    if equals(myAoriB, AoriB) and str(myAoriB) == str(AoriB):
        rez += 'Inmultire corecta \n'
    else:
        rez += 'Inmultire gresita \n'

    return rez