num = 11


if num > 1 :
    for i in range(2, num/2):
        if (num % i ) == 0 :
            print(num ," is not prime!")
            break
    else:
        print(num, " is prime ")
else :
    print(num," not prime")