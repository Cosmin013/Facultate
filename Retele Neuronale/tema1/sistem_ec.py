
def parsare():
    rez = []
    B = []
    with open("ec.txt") as fp:
        line = fp.readline()
        while line:
            a, b, c, r = 0, 0, 0, 0
            cut = 0
            for i in range(len(line)):
                if line[i] == 'a':
                    if line[cut:i] == '' or line[cut:i] == '+':
                        a = 1
                        cut = i+1
                    elif line[cut:i] == '-':
                        a = (-1)
                        cut = i + 1
                    else:
                        a = int(line[cut:i])
                        cut = i + 1
                if line[i] == 'b':
                    if line[cut:i] == '' or line[cut:i] == '+':
                        b = 1
                        cut = i + 1
                    elif line[cut:i] == '-':
                        b = (-1)
                        cut = i + 1
                    else:
                        b = int(line[cut:i])
                        cut = i + 1
                if line[i] == 'c':
                    if line[cut:i] == '' or line[cut:i] == '+':
                        c = 1
                        cut = i+1
                    elif line[cut:i] == '-':
                        c = (-1)
                        cut = i + 1
                    else:
                        c = int(line[cut:i])
                        cut = i + 1
                if line[i] == '=':
                    r = int(line[i+1:])
                    break

            rez.append([a, b, c])
            B.append(r)
            line = fp.readline()

    rez.append(B)
    return rez


def determiant(m):
    d = m[0][0] * m[1][1] * m[2][2] + m[0][1] * m[1][2] * m[2][0] + m[0][2] * m[1][0] * m[2][1]
    d = d - (m[0][2] * m[1][1] * m[2][0] + m[0][1] * m[1][0] * m[2][2] + m[0][0] * m[1][2] * m[2][1])
    return d



def transpusa(m):
    trans = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(len(m)):
        for j in range(i, len(m)):
            trans[i][j] = m[j][i]
            trans[j][i] = m[i][j]
    return trans

def det2(m, sign):
    return sign*(m[0] * m[3] - m[1] * m[2])


def adj(m):
    A_adj = []
    sign = 1
    for i in range(3):
        for j in range(3):
            mini = []
            for k in range(3):
                for l in range(3):
                    if i != k and j != l:
                        mini.append(m[k][l])
            A_adj.append(det2(mini, sign))
            sign = sign*(-1)
    return A_adj

def impart(m, d):
    a = []
    for i in range(len(m)):
        a.append(m[i]/d)
    return a

def inmultire(m, n):
    rez = [0, 0, 0];
    for i in range(3):
        for j in range(3):
            rez[i] += m[i*3 + j] * n[j]
    return rez


if __name__ == "__main__":
    mat = parsare()
    print(mat)
    B = mat.pop()
    det = determiant(mat)
    if det != 0:
        A_trans = transpusa(mat)
        A_adj = adj(A_trans)
        A_inv = impart(A_adj, det)
        print(inmultire(A_inv, B))

'''
- functie de acuratete...
    adunam locurile de unde a dat ok, - greseli...
    ....
o singura inmultire pt toti neuronii :D

acuratete > 95%

'''