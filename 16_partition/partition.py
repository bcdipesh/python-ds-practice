def partition(lst, fn):
    """Partition lst by predicate.

     - lst: list of items
     - fn: function that returns True or False

     Returns new list: [a, b], where `a` are items that passed fn test,
     and `b` are items that failed fn test.

        >>> def is_even(num):
        ...     return num % 2 == 0

        >>> def is_string(el):
        ...     return isinstance(el, str)

        >>> partition([1, 2, 3, 4], is_even)
        [[2, 4], [1, 3]]

        >>> partition(["hi", None, 6, "bye"], is_string)
        [['hi', 'bye'], [None, 6]]
    """

    # make 2 new list
    passed_list = []
    failed_list = []

    # loop over each element in the lst
    for element in lst:
        # for each element if the current element passed the fn add it to passed_list
        if fn(element) == True:
            passed_list.append(element)
        # else add it to failed_list
        else:
            failed_list.append(element)

    # return a new list with passed_list and failed_list
    return [passed_list, failed_list]
