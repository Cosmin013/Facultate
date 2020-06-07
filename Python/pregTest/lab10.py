import sys
import datetime
import random
import math
import timeit

def ex1_aux(args):
    if args[2] == '+':
        return int(args[1]) + int(args[3])
    if args[2] == '/':
        return int(args[1]) / int(args[3])
    if args[2] == '*':
        return int(args[1]) * int(args[3])
    if args[2] == '%':
        return int(args[1]) % int(args[3])

def ex1():
    res = ex1_aux(sys.argv)
    now = datetime.datetime.now()

    file = open(sys.argv[4], 'w')

    file.write(str(now) + ' ' + sys.argv[1] + ' ' + sys.argv[2] + ' ' + sys.argv[3] + ' = ' + str(res))


def ex2():
    max_nr = int(sys.argv[1])
    draw_size = int(sys.argv[2])
    nr_players = int(sys.argv[3])

    winning_num = [random.randint(1, max_nr) for i in range(draw_size)] # random.randint(a, b) Return a random integer N such that a <= N <= b.

    num_players = [[random.randint(1, max_nr) for i in range(draw_size)] for j in range(nr_players)]

    scores = [0 for i in range(draw_size)]

    for player in range(nr_players):
        for num in num_players[player]:
            if num in winning_num:
                scores[player] += 1

    print(winning_num)
    print(scores)
    for player in range(len(num_players)):
        print("player", player + 1,":" ,num_players[player])

def ex3():
    path1 = sys.argv[1]
    path2 = sys.argv[2]
    path3 = sys.argv[3]

    file1 = open(path1, 'r').readlines()
    file2 = open(path2, 'r').readlines()
    file3 = open(path3, 'r').readlines()

    teams1 = [team.rstrip() for team in file1] # .rstrip() elimina \n de la finalul string-ului
    teams2 = [team.rstrip() for team in file2]
    date_list = [time.rstrip() for time in file3]

    while teams1 and teams2 and date_list:
        # cu choice
        # team1 = random.choice(teams1)
        # team2 = random.choice(teams2)
        # date = random.choice(date_list)
        #
        # print(date, team1, team2)
        #
        # teams1.remove(team1)
        # teams2.remove(team2)
        # date_list.remove(date)

        # cu index
        team1 = random.randint(0, len(teams1) - 1)
        team2 = random.randint(0, len(teams2) - 1)
        date = random.randint(0, len(date_list) - 1)

        print(date_list[date], teams1[team1], teams2[team2])

        teams1.pop(team1)
        teams2.pop(team2)
        date_list.pop(date)

def ex4():
    arrival_time_str = "25 dec 2020 03:33:33"
    arrival_time_obj = datetime.datetime.strptime(arrival_time_str, "%d %b %Y %H:%M:%S")

    # "Jun 28 2018 at 7:40AM" -> "%b %d %Y at %I:%M%p"
    # "September 18, 2017, 22:19:55" -> "%B %d, %Y, %H:%M:%S"
    # "Sun,05/12/99,12:30PM" -> "%a,%d/%m/%y,%I:%M%p"
    # "Mon, 21 March, 2015" -> "%a, %d %B, %Y"
    # "2018-03-12T10:12:45Z" -> "%Y-%m-%dT%H:%M:%SZ"

    print(arrival_time_obj.date())
    print(arrival_time_obj.time())

    print((arrival_time_obj - datetime.datetime.now()).total_seconds())

def ex5():
    date = datetime.datetime(int(sys.argv[1]), 1, 1) # an, luna, zi...

    print(date.weekday()) # 0 luni, 6 duminica... trb facute if-uri

def isprime1(n):
    for i in range(2, n):
        if (n % i) == 0:
            return True
    return False

def isprime2(n):
    for i in range(2, int(math.sqrt(n))):
        if (n % i) == 0:
            return True
    return False

def ex6():
    n = 7919
    start = timeit.timeit()
    res1 = isprime1(n)
    mid = timeit.timeit()
    res2 = isprime2(n)
    stop = timeit.timeit()

    f1_time = start - mid
    f2_time = mid - stop

    print(f1_time, res1)
    print(f2_time, res2)


if __name__ == "__main__":
    ex6()
