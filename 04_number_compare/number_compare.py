def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """

    # check if a and b are equal
    if (a == b):
        # if equal return Numbers are equal
        return "Numbers are equal"
    # if not equal check if a is greater than b
    elif (a > b):
        # if greater return First is greater
        return "First is greater"
    # if code execution reached this line means b is greater return Second is greater
    else:
        return "Second is greater"
