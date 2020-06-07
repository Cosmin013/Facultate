import state_class as state
import numpy as np
import itertools


def str_rand(s):
    visited = [s]
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
        if count == 10000:
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
    if s.is_final():
        done.append(s)
        return True
    if depth < limit:
        for i in range(b+1):
            for j in range(b + 1):
                mm = ((-1) ** s.get_bp()) * j
                cm = ((-1) ** s.get_bp()) * i
                if s.validation(mm, cm):
                    ns = s.transition(mm, cm)
                    if str_idfs(ns, b, visited, limit, depth, done):
                        done.append(s)
                        return True

    return False


def idfs_main(s):
    i = 2
    done = [False]
    while True:
        print(i)
        if str_idfs(s, s.get_b(), list(), i, 0, done):
            done.pop(0)
            done.reverse()
            return done
        i += 2
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
    nm = s.get_nm1;
    nc = s.get_nm1;
    d = [[s, 1, s]]
    while q:
        v = q.pop()
        neighbours = list(itertools.product(range(b + 1), repeat=2))
        index_v = find_in_d(v, d)
        sign = ((-1) ** v.get_bp())
        for neighbour in neighbours:
            if v.validation(sign * neighbour[0], sign * neighbour[1]):
                ns = v.transition(sign * neighbour[0], sign * neighbour[1])



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



        q.sort(key=lambda node: d[find_in_d(node, d)][1] + h(node), reverse=True)

    return d[find_in_d(state.State(b, 0, 0, 2, nm, nc), d)]


if __name__ == "__main__":
    a = state.State(5, 15, 15)
    for i in idfs_main(a):
        print(i)

