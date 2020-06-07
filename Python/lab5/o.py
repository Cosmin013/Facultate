#1)
#app.py

from utils import process_item

runnning = True
while runnning:
    nr = input("Number:")
    if nr == "q":
        runnning = False
    else:
        print(process_item(int(nr)))


###utils.py

def process_item(x):
    found = 0
    while found == 0:
        x += 1
        prim = True
        for div in range(2, int(x / 2)):
            if x % div == 0:
                prim = False

        if prim == True:
            found = 1

    return x


if __name__ == "__main__":
    number = input("Number:")
    print(process_item(int(number)))


def sum_parametrii_variabili(*a, **k):
    suma = 0
    for j in k.keys():
        suma = suma + k[j]
    return suma


lambda_suma = lambda *a, **k: sum(list(k.values()))


####################### ex 3

def f1(arg):
    rez = []
    for chr in arg:
        if chr.lower() in ['a', 'i', 'u', 'e', 'o']:
            rez.append(chr)
    return rez


f2 = lambda arg: [chr for chr in arg if chr.lower() in ['a', 'i', 'u', 'e', 'o']]

f3 = lambda arg: list(filter(lambda chr: "aiueo".count(chr.lower()) > 0, arg))


def isvocala(caracter):
    if caracter in ["a", "e", "i", "o", "u"]:
        return True
    else:
        return False


def functie_vocale_filter(sir):
    return (list(filter(isvocala, sir)))


############################# ex 4

def fd(*args, **kargs):
    rez = []

    def check(d):
        if type(d) == dict and len(d) >= 2:
            for key in d:
                if type(key) == str and len(key) >= 3:
                    return True
        return False

    for arg in args:
        if check(arg):
            rez.append(arg)

    for key, value in kargs.items():
        if check(value):
            rez.append(value)

    return rez


def fd2(*args, **kargs):
    rez = []

    aux = list(filter(lambda arg: type(arg) == dict, args))
    aux = list(filter(lambda arg: len(arg) >= 2, aux))
    aux = list(
        filter(lambda arg: len(list(filter(lambda key: type(key) == str and len(key) >= 3, arg.keys()))) > 0, aux))

    rez += aux

    aux = list(filter(lambda arg: type(arg) == dict, kargs.values()))
    aux = list(filter(lambda arg: len(arg) >= 2, aux))
    aux = list(
        filter(lambda arg: len(list(filter(lambda key: type(key) == str and len(key) >= 3, arg.keys()))) > 0, aux))

    rez += aux

    return rez