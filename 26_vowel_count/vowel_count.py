def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}

        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    # make a set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}

    # make a empty dictionary
    freq_count = {}

    # change the phrase to lowercase
    phrase = phrase.lower()

    # remove all the whitespaces from the phrase
    phrase = phrase.replace(' ', '')

    # make a list of character from the phrase
    phrase_list = list(phrase)

    # loop over all the character from the phrase_list
    for character in phrase_list:
        # for each character check if it is a vowel
        if character in vowels:
            # if it is a vowel check if it is present in the dictionary
            if character not in freq_count:
                # if it is not present count the number of occurrence of the character in the phrase and add it as a key/value pair in the dictionary
                freq_count[character] = phrase_list.count(character)

    # return the dictionary
    return freq_count
