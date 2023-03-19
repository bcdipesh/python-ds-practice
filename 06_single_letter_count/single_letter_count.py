def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """

    # uppercase the word and convert it to a list
    word_list = list(word.upper())
    # uppercase the letter
    letter = letter.upper()
    # use list count method to count the occurrence of letter in the list
    # return the count
    return word_list.count(letter)
