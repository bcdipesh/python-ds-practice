def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    # convert each list to set
    set1 = set(l1)
    set2 = set(l2)

    # apply intersection on set1 and set2 and store the result
    result = set1 & set2

    # convert the result to a list and return
    return list(result)
