def problem1(my_list):
    odd = [element for element in my_list if element % 2 == 1]
    even = [element for element in my_list if element % 2 == 0]

    return list(zip(even, odd))

if __name__ == "__main__":
    print(problem1(	[2, 2, 2, 4, 5, 5, 5, 7, 7, 2, 4, 5, 7, 7, 4, 4]))