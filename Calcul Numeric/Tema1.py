import math
import random


def four_russians(A, B):
    n = len(A)
    m = math.floor(math.log(n))
    p = math.ceil(n/m)

    print(m, p)


    A_sectioned = [[[A[j][i] if i < n else 0 for i in range(m * k, m * (k + 1))] for j in range(n)] for k in
                   range(0, p)]

    B_sectioned = [[[B[j][i] if j < n else 0 for i in range(n)] for j in range(m * k, m * (k + 1))] for k in
                   range(0, p)]




n = 8

A = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]
B = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]


for i in A:
    print(i)

print()

for i in B:
    print(i)

if __name__ == "__main__":
    four_russians(A, B)
