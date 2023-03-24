def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """

    # check the type of collection
    if isinstance(collection, (str, list, tuple)):
        # if it is a string, list or tuple check if start index is provided
        if start is not None:
            # if that is the case start searching from that index
            # loop through the collection starting from the given index till end
            for index in range(start, len(collection)):
                # for each element check if it matches the sought element
                if collection[index] == sought:
                    # if it does return True
                    return True
        # else start searching from the start
        else:
            # loop through the collection till the end
            for element in collection:
                # for each element check if it matches the sought element
                if element == sought:
                    # if it does return True
                    return True
    # elif check if the collection is a set
    elif isinstance(collection, set):
        # if that is the case return True if sought value is present
        if sought in collection:
            return True
    # elif check if the collection is a dictionary
    elif isinstance(collection, dict):
        # if that is the case loop over the values of the dict
        for value in collection.values():
            # for each value check if it matches the sought value
            if value == sought:
                # if it does return True
                return True

    # if code reached this line return False
    return False
