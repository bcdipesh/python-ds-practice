def sum_floats(nums):
    """Return sum of floating point numbers in nums.

        >>> sum_floats([1.5, 2.4, 'awesome', [], 1])
        3.9

        >>> sum_floats([1, 2, 3])
        0
    """

    # hint: to find out if something is a float, you should use the
    # "isinstance" function --- research how to use this to find out
    # if something is a float!

    # declare a variable called total_sum and initialize it to 0
    total_sum = 0

    # loop over num in nums
    for num in nums:
        # for each num check if it is a float
        if isinstance(num, float):
            # if this is the case then add it with the total_sum and store the result in total_sum
            total_sum += num

    # return total_sum
    return total_sum
