def linear_search(the_list, target):
    for i in range(len(the_list)):
        if the_list[i] == target:
            print("Found at index", i)
            return i
    print("Target is not in list")
    return -1


my_list = [5, 4, 63, 35, 7, 19, 23]
linear_search(my_list, 19)
linear_search(my_list, 63)
linear_search(my_list, 194)
