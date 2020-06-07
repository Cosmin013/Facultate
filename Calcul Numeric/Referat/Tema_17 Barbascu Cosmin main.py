
import numpy as np

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


    return res

def read_b(path):
    f = open(path, "r+")
    res = list()

    for content in f.readlines()[1:-1]:
        res.append(float(content))

    return res

def multy(A, v):
    res = list()
    for i in range(len(A)):
        suma = 0
        for j in range(len(A[i])):
            suma += A[i][j][0] * v[A[i][j][1]]
        res.append(suma)
    return res


def GMRES_method(A, b, nr_iteratii):
    x0 = [0 for _ in range(len(b))]
    r = np.array(b) - np.array(multy(A, x0))
    x = list()
    q = [0 for _ in range(nr_iteratii)]
    q[0] = r / np.linalg.norm(r)
    h = np.zeros((nr_iteratii + 1, nr_iteratii))
    for k in range(nr_iteratii):
        y = multy(A, q[k])
        for j in range(k):
            h[j, k] = np.dot(q[j], y)
            y = y - h[j, k] * q[j]
        h[k + 1, k] = np.linalg.norm(y)
        if (h[k + 1, k] != 0 and k != nr_iteratii - 1):
            q[k + 1] = y / h[k + 1, k]

        b = np.zeros(nr_iteratii + 1)
        b[0] = np.linalg.norm(r)

        result = np.linalg.lstsq(h, b, rcond=-1)[0]

        x.append(np.dot(np.asarray(q).transpose(), result) + x0)
    return x


if __name__ == '__main__':
    A = read_sparse_matrix("a_2.txt")
    b = read_b("b_2.txt")
    print(GMRES_method(A, b, 100)[:-1])
