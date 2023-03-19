def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    # turn the string into individual characters list
    str_list = list(phrase)
    # get characters from last to first with list slicing, join the resulting list into new str and return
    return "".join(str_list[::-1])
