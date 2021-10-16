def linear_search_dictionary(dictionary, target):
    for key, value in dictionary.items():
        if value == target:
            print("Found at key {}".format(key))
            return key
    print("Target not found in dictionary")
    return -1

my_dictionary = {"red": 5, "blue": 3, "yellow": 12, "green": 7}
linear_search_dictionary(my_dictionary, 5)
linear_search_dictionary(my_dictionary, 3)
linear_search_dictionary(my_dictionary, 8)