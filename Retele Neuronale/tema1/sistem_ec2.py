
import numpy as np

def parsare():
    rez = []
    B = []
    with open("ec.txt") as fp:
        line = fp.readline()

        while line:
            a, b, c, r = 0, 0, 0, 0
            cut = 0
            for i in range(len(line)):
                if line[i:i+1] == 'a':
                    if line[cut:i] == '' or line[cut:i] == '+':
                        a = 1
                        cut = i+1
                    elif line[cut:i] == '-':
                        a = (-1)
                        cut = i + 1
                    else:
                        a = int(line[cut:i])
                        cut = i + 1
                if line[i:i+1] == 'b':
                    if line[cut:i] == '' or line[cut:i] == '+':
                        b = 1
                        cut = i + 1
                    elif line[cut:i] == '-':
                        b = (-1)
                        cut = i + 1
                    else:
                        b = int(line[cut:i])
                        cut = i + 1
                if line[i:i+1] == 'c':
                    if line[cut:i] == '' or line[cut:i] == '+':
                        c = 1
                        cut = i+1
                    elif line[cut:i] == '-':
                        c = (-1)
                        cut = i + 1
                    else:
                        c = int(line[cut:i])
                        cut = i + 1
                if line[i:i+1] == '=':
                    r = int(line[i+1:])
                    break

            rez.append([a, b, c])
            B.append(r)
            line = fp.readline()

    rez.append(B)
    return rez



def adj(m):
    ad = [[0 for i in range(3)] for j in range(3)]
    s = 1
    for i in range(3):
        for j in range(3):
            mini = []
            for k in range(3):
                for l in range(3):
                    if i != k and j != l:
                        mini.append(m[k][l])
            ad[i][j] = np.linalg.det(np.array(mini).reshape(2, 2)) * s
            s = s*(-1)
    return ad



if __name__ == "__main__":
    m = parsare()
    print(m)
    B = np.array(m.pop()).transpose()
    A = np.array(m, dtype=int)
    det = np.linalg.det(A)
    if det != 0:
        trans = np.matrix.transpose(A)
        A_adj = adj(trans)
        #A_inv = np.dot(A_adj, det**(-1))
        A_inv = np.true_divide(A_adj, det)
        rez = np.matmul(A_inv, B)
        print(rez)

    ''''
    A_inv= np.linalg.inv(A)
    print(np.linalg.solve(A,np.transpose(B)))
    '''
    exit()
