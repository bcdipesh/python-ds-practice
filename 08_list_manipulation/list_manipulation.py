def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    # lowercase the command and location value
    command = command.lower()
    location = location.lower()
    # check if command is "remove"
    if command == "remove":
        # if this is the case check if location is "beginning"
        if location == "beginning":
            # if this is the case remove the element from the beginning of the list and return it
            return lst.pop(0)
        # elif check if location is "end"
        elif location == "end":
            # if this is the case remove the element from the end of the list and return it
            return lst.pop()
        # if the code execution reached this line return None
        else:
            return None
    # check if command is "add"
    elif command == "add":
        # if this is the case check if value is not None
        if value is not None:
            # if this is the case check if location is "beginning"
            if location == "beginning":
                # if this is the case add value to the beginning of the list and return the list
                lst.insert(0, value)
                return lst
            # elif check if location is "end"
            elif location == "end":
                # if this is the case add value to the end of the list and return the list
                lst.append(value)
                return lst
            # if the code execution reached this line return None
            else:
                return None
    # if the code execution reached this line return None
    else:
        return None
