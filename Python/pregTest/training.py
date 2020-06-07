import urllib
from urllib import request
import re
import os
from hashlib import md5
import sys


def problema1(s):
    lista = re.findall(r"[_A-Za-z\d]+", s)
    lista.sort()
    return lista

def problema2(s, url):
    try:
        response = urllib.request.urlopen(url).read()
        text = response.decode("utf-8")
        if s in text:
            return True
        return False
    except Exception as e:
        return False



def problema3(path):
    res = list()
    files = os.listdir(path)
    paths = [ os.path.join(path, file)  for file in files]
    for path in paths:
        if os.path.isfile(path):
            res.append(md5(open(path, 'rb')))




if __name__ == "__main__":
   # print(problema1("test str_ing"))
   # print(problema2("ceva", "http://www.info.uaic.ro/bin/Structure/Management"))
   file = open("test12.txt", 'a+')
   print(file.tell())