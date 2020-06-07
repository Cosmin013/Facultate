def problema1(my_list):
    odd = [element for element in my_list if element % 2 == 1]
    even = [element for element in my_list if element % 2 == 0]

    return zip(odd,even)