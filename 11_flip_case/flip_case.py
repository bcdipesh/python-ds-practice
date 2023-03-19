def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    # convert the phrase to a list and store it in phrase_list
    phrase_list = list(phrase)
    swapped_phrase_list = []

    # loop through the phrase_list
    for ch in phrase_list:
        # for each character in the list uppercase both the character and to_swap and compare if both are equal
        if ch.upper() == to_swap.upper():
            # if this is the case swap the case of the character and add it to swapped_phrase_list
            swapped_phrase_list.append(ch.swapcase())
        # else just add the character as it is to swapped_phrase_list
        else:
            swapped_phrase_list.append(ch)

    # join the items inside the swapped_phrase_list and return it as a string
    return ''.join(swapped_phrase_list)
