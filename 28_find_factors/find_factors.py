def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """

    # create an empty list called factors
    factors = []

    # run a loop through 1 to num
    for number in range(1, num + 1):
        # check if current number is a factor of num
        if num % number == 0:
            # if that is the case add the number to factors
            factors.append(number)

    # return the factors
    return factors
