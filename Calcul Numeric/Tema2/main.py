import numpy as np
import random as rand

t = 10
eps = 10 ** (-t)

res = str()


def descompunereLU(A, n):
    # calculam descompunerea LU direct in matricea A
    for p in range(0, n):
        for i in range(p, n):
            A[p][i] = A[p][i] - sum(A[p][k] * A[k][i] for k in range(0, p))
        for j in range(p+1, n):
            if np.abs(A[p][p] > eps):
                A[j][p] = (1/A[p][p])*(A[j][p] - sum(A[j][k] * A[k][p] for k in range(0, p)))
            else:
                return []
    return A

# print(descompunereLU([[2.5, 2, 2, 2], [5, 6, 5, 5], [5, 6, 6.5, 1], [3, 9, 2, 2]], 4))


def determinantA(A, n):
    detA = 1
    if A:
        for i in range(0, n):
            # matricile L, U sunt triunghiulare, iar determinantul este produsul elementelor de pe diagonala principala
            # L are doar 1 pe diagonala, deci detA=detU
            detA *= A[i][i]
        return detA
    return 0

# print(determinantA(descompunereLU([[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5], [3, 9, 2]], 3), 3))


def rezolvare_sistem(A, n, b):
    if A:
        # aflam y din ecuatia Ly = b
        y = [0]*n
        for i in range(0, n):
            y[i] = (b[i] - sum(A[i][j] * y[j] for j in range(0, i)))

        # aflam x din ecuatia Ux = y
        x = [0]*n
        for i in range(n-1, -1, -1):
            if np.abs(A[i][i] > eps):
                x[i] = (y[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]
            else:
                print("Nu se poate face impartirea. Matricea are un minor null.")
                return []
        return x

# print(rezolvare_sistem(descompunereLU([[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]], 3), 3, [2, 2, 2]))


def norma_euclidiana(z):
    return np.sqrt(sum(elem**2 for elem in z))


def verificare_solutie(A_init, x_lu, b_init, n):
    y = [0] * n
    for i in range(0, n):
        y[i] = sum(A_init[i][j] * x_lu[j] for j in range(0, n))

    if norma_euclidiana(np.subtract(y, b_init)) < 10**(-8) or norma_euclidiana(np.subtract(y, b_init)) < 10**(-9):
        return "solutie corecta"
    return "solutie incorecta"

# print(verificare_solutie([[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]], rezolvare_sistem(descompunereLU([[2.5, 2, 2], [5,
# 6, 5], [5, 6, 6.5]], 3), 3, [2, 2, 2]), [2, 2, 2], 3))


def inversa_lib_matrice(A, x_lu, b):
    global res
    x_lib = np.linalg.solve(A, b)
    res += "Solutia sistemului folosind biblioteca numpy: " + str(list(x_lib)) + "\n"
    A_lib_invers = np.linalg.inv(A)
    res += "Norma euclidiana (x_lu - x_lib): " + str(norma_euclidiana(np.subtract(x_lu, x_lib))) + "\n"
    res += "Norma euclidiana (x_lu - A_lib_invers*b_init): " + str(norma_euclidiana(np.subtract(x_lu, np.dot(A_lib_invers, b)))) + "\n"
    return A_lib_invers

# print(inversa_lib_matrice([[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]], 3, [2,2,2]))


def inversa_lu_matrice(A_lu, n):
    inversa = list()
    for i in range(0, n):
        e = [0] * n
        e[i] = 1
        x = rezolvare_sistem(A_lu, n, np.transpose(e))
        inversa.append(x)
    return np.transpose(inversa)

# print(inversa_lu_matrice(descompunereLU([[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]], 3), 3))


def get_output(n, A, b):
    global res
    A_init = np.copy(A)  # retinem matricea initiala A

    A = descompunereLU(A, n)
    if A:  # daca exista descompunere LU facem si celelalte calcule
        res += "Descompunerea LU a matricei A: \n"  # afisam matricea A care contine descompunerea LU
        for row in A:
            res += str(row) + '\n'

        detA = determinantA(A, n)  # calculam det matricei A folosind descompunerea LU
        res += "Determinantul matricei A folosind LU: " + str(detA) + "\n"

        x_lu = rezolvare_sistem(A, n, b)
        res += "Solutia aprox. a sistemului folosind LU: " + str(x_lu) + "\n"

        res += "Verificare solutie cu norma euclidiana: " + str(x_lu) + ' ' + str(verificare_solutie(A_init, x_lu, b, n)) + "\n"

        A_lib_inversa = inversa_lib_matrice(A_init, x_lu, b)
        A_lu_inversa = inversa_lu_matrice(A, n)
        res += "Inversa matricei A folosind LU: \n"
        for row in A_lu_inversa:
            res += str(row) + "\n"

        z = np.subtract(A_lu_inversa, A_lib_inversa)
        res += "Norma (A_lu_inversa - A_lib_inversa): " + str(max(sum(np.abs(z[i][j]) for i in range(0, n)) for j in range(0, n))) + "\n"
    else:
        res += "Nu se poate face impartirea. Matricea are un minor null."

    return res


if __name__ == '__main__':
    n = 3
    A = [[2.5, 2, 2], [5, 6, 5], [5, 6, 6.5]]
    b = [2, 2, 2]
    get_output(n, A, b)
