def find_the_duplicate(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate([2, 1, 3, 4]) is None
        True
    """

    # loop over each numbers in nums
    for number in nums:
        # for each number check the count of number in nums
        if nums.count(number) > 1:
            # if it is greater than 1 return the number
            return number

    # if code reached here return None
    return None
