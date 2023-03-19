def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    # use range to loop over num in nums
    for x in range(len(nums)):
        # use range to loop over num in nums that ends before last index
        for y in range(len(nums) - 1):
            # check if the sum of num from the outerloop and num from innerloop is equal to goal
            if nums[x] + nums[y+1] == goal:
                # if that is the case return a tuple that contains those num
                return (nums[x], nums[y+1])

    # return empty tuple
    return ()
