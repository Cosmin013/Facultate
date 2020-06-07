import state_class as state
import numpy as np
import itertools
import time


def str_rand(s):
    if s.get_nc1() <= s.get_nm1():
        visited = [s]
    else:
        return False

    count = 0
    while not s.is_final():
        mm = ((-1) ** s.get_bp()) * np.random.randint(0, s.get_b() + 1)
        cm = ((-1) ** s.get_bp()) * np.random.randint(0, s.get_b() + 1)
        count += 1
        if s.validation(mm, cm) and not visited.count(s.transition(mm, cm)):
            s = s.transition(mm, cm)
            visited.append(s)
            count = 0
            if len(visited) == 100:
                s = visited[0]
                visited = [s]
        if count == 1000:
            s = visited[0]
            visited = [s]
            count = 0

    return visited


def str_bktr(s):
    visited = [s]
    stack = [s]
    b = s.get_b()
    while stack:
        s = stack[len(stack) - 1]
        mm = 0
        while mm <= b:
            cm = 0
            while cm <= b:
                sign = (-1) ** (s.get_bp())
                if s.validation(sign * mm, sign * cm) and not visited.count(s.transition(sign * mm, sign * cm)):
                    s = s.transition(sign * mm, sign * cm)
                    visited.append(s)
                    stack.append(s)
                    if s.is_final():
                        return stack
                    mm, cm = 0, -1
                cm += 1
            mm += 1
        stack.pop()

    return 0


def str_idfs(s, b, visited, limit, depth, done):
    depth += 1
    visited.append(s)
    if s.is_final():
        done.append(s)
        return True
    if depth < limit:
        v = list(itertools.product(range(b + 1), repeat=2))
        v.pop(0)
        while v:
            n = np.random.randint(len(v))
            mm = ((-1) ** s.get_bp()) * v[n][0]
            cm = ((-1) ** s.get_bp()) * v[n][1]
            if s.validation(mm, cm) and not visited.count(s.transition(mm, cm)):
                ns = s.transition(mm, cm)
                if str_idfs(ns, b, visited, limit, depth, done):
                    done.append(s)
                    return True
            v.pop(n)
    elif done[0]:
        v = list(itertools.product(range(b + 1), repeat=2))
        v.pop(0)
        while v:
            n = np.random.randint(len(v))
            mm = ((-1) ** s.get_bp()) * v[n][0]
            cm = ((-1) ** s.get_bp()) * v[n][1]
            if s.validation(mm, cm) and not visited.count(s.transition(mm, cm)):
                done[0] = False
                break
            v.pop(n)
    return False


def idfs_main(s):
    i = 2
    done = [False]
    while not done[0]:
        done[0] = True
        if str_idfs(s, s.get_b(), list(), i, 0, done):
            done.pop(0)
            done.reverse()
            return done
        i += 2
        print(i)
    return False


def h(s):
    return s.get_nm1() + s.get_nc1()


def find_in_d(a, d):
    for i in range(len(d)):
        if d[i][0] == a:
            return i
    return -1


def str_A(s):
    q = [s]
    b = s.get_b()
    d = [[s, 1, s]]
    while q:
        v = q.pop()
        neighbours = list(itertools.product(range(b + 1), repeat=2))
        index_v = find_in_d(v, d)
        sign = ((-1) ** v.get_bp())
        for neighbour in neighbours:
            if v.validation(sign * neighbour[0], sign * neighbour[1]):

                ns = v.transition(sign * neighbour[0], sign * neighbour[1])

                if ns.is_final():
                    return d[index_v][2:] + [ns]

                if find_in_d(ns, d) == -1:
                    d.append([ns, d[index_v][1] + 1])
                    index_ns = find_in_d(ns, d)
                    d[index_ns] += d[index_v][2:] + [ns]
                    q.append(ns)

                else:
                    index_ns = find_in_d(ns, d)
                    if d[index_v][1] + 1 < d[index_ns][1]:
                        d[index_ns][1] = d[index_v][1] + 1
                        d[index_ns] = d[index_ns][:2] + d[index_v][2:] + [ns]

        q.sort(key=lambda node: d[find_in_d(node, d)][1] + h(node))
    return False


if __name__ == "__main__":
    instances = []
    for i in range(1, 11):
        b = np.random.randint(2, 6)
        nm = np.random.randint(3, 16)
        nc = np.random.randint(3, 16)

        while (b, nm, nc) in instances:
            b = np.random.randint(2, 6)
            nm = np.random.randint(3, 16)
            nc = np.random.randint(3, 16)
        else:
            instances.append((b, nm, nc))

    len_random = 0
    solution_count_random = 0
    duration_random = 0
    for i in instances:
        start = time.time()
        a = state.State(i[0], i[1], i[2])
        print(i)
        rez = str_rand(a)

        if rez:
            len_random = len_random + len(rez)
            solution_count_random += 1
            print("Random strategy return:")
            for j in rez:
                print(j)
            print(" ")
        else:
            print("No Solution Found for random strategy!")
            print(" ")
        stop = time.time()
        duration_random = duration_random + stop - start

    len_bkt = 0
    solution_count_bkt = 0
    duration_bkt = 0
    for i in instances:
        start = time.time()
        a = state.State(i[0], i[1], i[2])
        print(i)
        rez = str_bktr(a)

        if rez:
            len_bkt = len_bkt + len(rez)
            solution_count_bkt += 1
            print("BKT strategy return:")
            for j in rez:
                print(j)
            print(" ")
        else:
            print("No Solution Found for bkt strategy!")
            print(" ")
        stop = time.time()
        duration_bkt = duration_bkt + stop - start

    len_idfs = 0
    solution_count_idfs = 0
    duration_idfs = 0
    for i in instances:
        start = time.time()
        a = state.State(i[0], i[1], i[2])
        print(i)
        rez = idfs_main(a)

        if rez:
            len_idfs = len_idfs + len(rez)
            solution_count_idfs += 1
            print("Idfs strategy return:")
            for j in rez:
                print(j)
        else:
            print("No Solution Found for idfs strategy!")
        stop = time.time()
        duration_idfs = duration_idfs + stop - start

    len_A = 0
    solution_count_A = 0
    duration_A = 0
    for i in instances:
        start = time.time()
        a = state.State(i[0], i[1], i[2])
        print(i)
        rez = str_A(a)

        if rez:
            len_A = len_A + len(rez)
            solution_count_A += 1
            print("A strategy return:")
            for j in rez:
                print(j)
            print(" ")
        else:
            print("No Solution Found for A strategy!")
            print(" ")
        stop = time.time()
        duration_A = duration_A + stop - start

    print("Random strategy length:", len_random//solution_count_random, "and time: ", duration_random, solution_count_random)
    print("BKT strategy length:", len_bkt//solution_count_bkt, "and time: ", duration_bkt, solution_count_bkt)
    print("IDFS strategy length:", len_idfs//solution_count_idfs, " and time: ", duration_idfs)
    print("A strategy length:", len_A//solution_count_A, "and time: ", duration_A, solution_count_A)


