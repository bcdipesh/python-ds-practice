def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)

    """

    # convert operation to lowercase
    operation = operation.lower()

    # create a variable result
    result = None

    # check if operation is "add"
    if operation == "add":
        # if this is the case add a and b and store the result
        result = a + b

        # check if make_int is true
        if make_int == True:
            # if this is the case convert result to int
            result = int(result)
    # elif check if operation is "subtract"
    elif operation == "subtract":
        # if this is the case subtract a and b and store the result
        result = a - b

        # check if make_int is true
        if make_int == True:
            # if this is the case convert result to int
            result = int(result)
    # elif check if operation is "multiply"
    elif operation == "multiply":
        # if this is the case multiply a and b and store the result
        result = a * b

        # check if make_int is true
        if make_int == True:
            # if this is the case convert result to int
            result = int(result)
    # elif check if operation is "divide"
    elif operation == "divide":
        # if this is the case divide a and b and store the result
        result = a / b

        # check if make_int is true
        if make_int == True:
            # if this is the case convert result to int
            result = int(result)
    # else return result
    else:
        return result

    # return the result with the message provided
    return f"{message} {result}"
