def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # use list comprehension and create a new list that has truthy value and return it
    true_elements = [el for el in lst if el]

    return true_elements
