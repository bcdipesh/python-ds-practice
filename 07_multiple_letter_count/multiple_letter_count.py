def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    # convert phrase into a list
    phrase_list = list(phrase)
    # use list count method and dictionary comprehension to generate and return the desired output
    return {char: phrase_list.count(char) for char in phrase_list}
