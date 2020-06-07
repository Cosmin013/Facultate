
n = int(input())
rez = int(input())
for i in range(n-1):
    x = int(input())
    while x != rez :
        if x > rez :
            x = x - rez
        if rez > x :
            rez = rez - x
print(rez)


v = 'aeiou'
str = input()
counter = 0
for i in v:
    counter += str.count(i)

print(counter)






# 'ba' in 'abba' -> True
# 'abcda'.count('a') -> 2
# 'sdasd'.index('a')
# type(var) -> tipul vat..
# str[::2] -> din 2 in 2 de la 0
# str[0:5:2] -> ...
#split