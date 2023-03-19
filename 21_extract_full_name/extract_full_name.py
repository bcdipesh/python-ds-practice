def extract_full_names(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """

    # make a new list
    full_names = []

    # loop over people list
    for person in people:
        # for each people loop over current people dictionary keys
        # declare a variable called full_name and initialize it to empty str
        full_name = ""
        for key in person.keys():
            # make a full name using the key and value pair for the current person
            full_name += person[key] + " "

        # remove the trailing white space
        full_name = full_name.rstrip()
        # add it to the list
        full_names.append(full_name)

    # return the new list
    return full_names
