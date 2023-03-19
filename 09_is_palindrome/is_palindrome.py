def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    # convert phrase to lowercase
    phrase = phrase.lower()

    # strip leading and trailing white spaces
    phrase = phrase.strip()

    # split the phrase on space into word list and store it in word_list
    word_list = phrase.split(' ')

    # check if the size of word_list is 1
    if len(word_list) == 1:
        # if this is the case phrase has no spaces and we need to split the phrase into individual characters
        word_list = list(phrase)

    # join the words on the list without space and store in phrase
    phrase = ''.join(word_list)

    # make a list of characters from the updated phrase and reverse it
    reversed_phrase = list(phrase)
    reversed_phrase.reverse()

    # join the reversed_phrase
    reversed_phrase = ''.join(reversed_phrase)

    # check and return True if phrase and reversed_phrase are equal else False
    return phrase == reversed_phrase
