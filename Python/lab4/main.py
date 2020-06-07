def sortedTuples(tuples):
    tuples.sort(key = lambda x: x[1])
    return tuples

def check_if_exists(names, needle):
    return True if list(filter(lambda t: t[1] == needle, names)) else False

dict = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "%": lambda a, b: a % b
}

dict2 = {
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}

def apply_operator(operator, a, b ):
    lb = dict[operator]
    return lb(a,b)


def check_if_exists(names, needle):
    return True if list(filter(lambda t: t[1] == needle, names)) else False


def parametru(lista, first_name):
    for i in lista:
        if i[1] is first_name:
            return True
        elif (i[1] > first_name):
            return False
    return False


def ex2(tuples, first_name):
    return len([item for item in tuples if item[1] == first_name]) != 0


def check_first_name_02(names, searched_first_name):
    return any(searched_first_name == x[1] for x in names)

def ex4(operator, *args, **kwargs):
    global dict2
    return dict2[operator](*args, **kwargs)

ex4("print_all",'1','2')

def dictFromDictionaries(dict):
    dictionar = {}
    for dic in dict:
        for key in dic:
            if (key in dictionar):
                dictionar[key].append(dic[key])
            else:
                dictionar[key] = []
                dictionar[key].append(dic[key])
    return dictionar


def print_dict(d, prefix = ""):
    for key, value in d.items():
        if type(value) == dict:
            print_dict(value, f"{prefix}'{key}' - ")
        else:
            print(f"{prefix}'{key}' - {value}")

def afisare_dictionar(dictionar, precedent):
    for i in dictionar:
        if isinstance(dictionar[i], dict):
            afisare_dictionar(dictionar[i], precedent + i + " - ")
        else:
            print(precedent + str(i) + " - " + str(dictionar[i]))

if __name__ == "__main__":
    tuples = [("r","t"),("v","i")]
    aux = sortedTuples(tuples)
    #print(existInTuples(aux,('a','i')))
    #print(apply_operator("/",1,2))
    dict["++"] = lambda a, b: a + b + 1
    #print(apply_operator("++", 1, 2))

    list_dictionaries = [{
        "a": "b",
        "c": "d"
    },{
        "a":"b",
        "e":"f"
    }]

    d = {
   'a': 1,
   'b':
   {
       'c': 3,
       'd':
       {
           'e': 5,
           'f': 6
       }
   }
}
    #print(dictFromDictionaries(list_dictionaries))
    #print(print_dict(d))
    #print(afisare_dictionar(d,''))