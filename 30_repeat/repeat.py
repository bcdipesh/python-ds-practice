def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """

    # check if num is a valid number and greater than or equal to 0
    if isinstance(num, int) and num >= 0:
        # if that is the case create a empty list called phrase_list
        phrase_list = []

        # loop for num times and append phrase to phrase_list for each iteration
        for _ in range(0, num):
            phrase_list.append(phrase)

        # create and return a str using join on phrase_list
        return ''.join(phrase_list)
    # else return None
    else:
        return None
