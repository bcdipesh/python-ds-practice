def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """

    # create an empty dictionary called final_dict
    final_dict = {}

    # loop over the length of the keys
    for index in range(0, len(keys)):
        # check if current index is greater than length of values
        if index > (len(values) - 1):
            # if that is the case add a new key/value pair where key is item at current index in keys and value is None
            final_dict[keys[index]] = None
        else:
            # for each index add a new key/value pair in final_dict where key is item at current index in keys,
            # and value is item at current index in values
            final_dict[keys[index]] = values[index]

    return final_dict
