def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    # loop over all elements in the list
    for element in lst:
        # for each element check if it is of type list
        if isinstance(element, list) != True:
            # if that is not the case return False
            return False

    # if code reached this line then return True
    return True
