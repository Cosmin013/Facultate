import random
import math
import numpy as np

eps = pow(10, -5)


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


def generate_sparse_matrix(n, p):
    res = [list() for _ in range(p)]
    for x in range(p):
        num_elements_line = random.randint(1, math.ceil((p - x)/10))
        ys = list(range(n))[x:]
        for _ in range(num_elements_line):
            if ys:
                y = random.choice(ys)
                ys.remove(y)
                val = random.uniform(10.0, 100000.0)
                res[x].append([val, y])
                if y < n:
                    res[y].append([val, x])
            else:
                break
    for i in range(len(res)):
        res[i].sort(key=lambda x: x[1])
    lenghts = list()
    for i in range(len(res)):
        lenghts.append(len(res[i]))
    print(max(lenghts), min(lenghts), sum(lenghts)/len(lenghts))
    return res



def verifica_simetrie(A):
    for i in range(len(A)):
        for j in range(len(A[i])):
            for element in A[A[i][j][1]]:
                if element[1] == i and abs(element[0] - A[i][j][0]) < eps:
                    break
            else:
                return False
    return True


def multy(A, v):
    res = list()
    v = list(v)
    for i in range(len(A)):
        suma = 0
        for j in range(len(A[i])):
            suma += A[i][j][0] * v[A[i][j][1]]
        res.append(suma)
    return res

def metoda_puterii(A):
    v = np.random.randn(len(A))
    v /= np.linalg.norm(v)
    w = multy(A, v)
    lamb = np.dot(w, v)
    k = 0
    maxK = 1000000
    while True:
        v = w / np.linalg.norm(w)
        w = multy(A, v)
        lamb = np.dot(w, v)
        k += 1
        if (np.linalg.norm(w - lamb * v) <= len(A) * eps) or (k > maxK):
            break
    return lamb, v

if __name__ == '__main__':
    p = int(input("p = "))
    n = int(input("n = "))
    fisiere = ["a_300.txt", "a_500.txt", "a_1000.txt", "a_1500.txt", "a_2020.txt"]

    if p == n and p > 500:
        A = generate_sparse_matrix(n, p)
        strucuturile_fisiereleor = list()
        for i in fisiere:
            strucuturile_fisiereleor.append(read_sparse_matrix(i))
    elif p == n:
        A = generate_sparse_matrix(n, p)
        print(metoda_puterii(A))

        fisier = int(input("nr fisier (0 - 4) :"))
        A = read_sparse_matrix(fisiere[fisier])
        print("Simetrica : " ,verifica_simetrie(A))
        print(metoda_puterii(A))



