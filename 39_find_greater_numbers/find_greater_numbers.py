def find_greater_numbers(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers([1, 2, 3])
        3

        >>> find_greater_numbers([6, 1, 2, 7])
        4

        >>> find_greater_numbers([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers([])
        0
    """

    # create a variable called times_followed and set it to 0
    times_followed = 0

    # loop over nums from the starting index
    for i in range(0, len(nums)):
        # loop over nums from current index + 1
        for j in range(i + 1, len(nums)):
            # check if current number from outer loop is smaller than current number in this loop
            if nums[i] < nums[j]:
                # if that is the case increate times_followed by 1
                times_followed += 1

    # return times_followed
    return times_followed
