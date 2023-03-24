def three_odd_numbers(nums):
    """Is the sum of any 3 sequential numbers odd?"

        >>> three_odd_numbers([1, 2, 3, 4, 5])
        True

        >>> three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0])
        True

        >>> three_odd_numbers([5, 2, 1])
        False

        >>> three_odd_numbers([1, 2, 3, 3, 2])
        False
    """

    # loop over nums from the start index
    for i in range(0, len(nums)):
        # create a variable named total and set it to 0
        total = 0
        # loop over nums from start index to start index + 3
        for j in range(i, i + 3):
            # check if index is out of range
            if ((i + 3) - 1) > len(nums) - 1:
                # if that is the case break from current loop
                break
            # sum numbers with in the range
            else:
                total += nums[j]
        # if the total is odd return True
        if total % 2 != 0:
            return True

    # if code reaches here return False
    return False
