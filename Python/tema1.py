def cmmdc(lis=[]):
    rez = lis[0]
    for i in range(1, len(lis)):
        while rez != lis[i]:
            if rez > lis[i]:
                rez = rez - lis[i]
            if lis[i] > rez:
                lis[i] = lis[i] - rez

if __name__ == "__main__":
    print(cmmdc([6, 12, 7, 2]))

