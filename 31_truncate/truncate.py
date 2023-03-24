def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.

    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.

        >>> truncate("Hello World", 6)
        'Hel...'

        >>> truncate("Problem solving is the best!", 10)
        'Problem...'

        >>> truncate("Yo", 100)
        'Yo'

    The smallest legal value of n is 3; if less, return a message:

        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """

    # check if n is greater than or equal to 3
    if n >= 3:
        # if that is the case create an empty list called phrase_list
        phrase_list = []

        # create an empty str called truncated_phrase
        truncated_phrase = ""

        # loop over the phrase up until n - 3 or length of the phrase
        for index in range(0, (n - 3 if len(phrase) >= n else len(phrase))):
            # for each character add it to the phrase_list
            phrase_list.append(phrase[index])

        # join the characters present in phrase_list and assign the result to truncated_phrase
        truncated_phrase = ''.join(phrase_list)

        # if length of phrase is same or longer than n add '...' at the end
        if len(phrase) >= n:
            truncated_phrase += '...'

        # return the truncated_phrase
        return truncated_phrase
    # else return a message that says 'Truncation must be at least 3 characters'
    else:
        return 'Truncation must be at least 3 characters'
