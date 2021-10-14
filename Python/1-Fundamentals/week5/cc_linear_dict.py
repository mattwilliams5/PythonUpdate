def linear_search_dictionary(my_dict, target):
    '''
        Create a linear search through a dictionary
    '''

    for item in my_dict:
        if my_dict[item] == target:
            print("Your item has been found", item)
            return
    print("Your item is lost")
    return -1


my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)
