def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> last_element([1, 2, 3])
        3

        >>> last_element([]) is None
        True
    """

    # check if list is empty
    if len(lst) == 0:
        # if it is empty return None
        return None
    # if not empty pop the last element from the list
    return lst.pop()
