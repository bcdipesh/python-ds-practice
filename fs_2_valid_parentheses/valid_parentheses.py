def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """

    # create a paren_count dictionary and initialize it with '(': 0 , ')':0
    paren_count = {'(': 0, ')': 0}

    # loop over each paren in the parens
    for paren in parens:
        # for each paren increase the corresponding value in pren_count
        paren_count[paren] = paren_count[paren] + 1

    # compare the value of '(' and ')' and return the result
    return paren_count['('] == paren_count[')']
