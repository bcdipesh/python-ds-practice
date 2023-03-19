def multiply_even_numbers(nums):
    """Multiply the even numbers.

        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48

        >>> multiply_even_numbers([3, 4, 5])
        4

    If there are no even numbers, return 1.

        >>> multiply_even_numbers([1, 3, 5])
        1
    """

    # create and initialize a variable named total to 1
    total = 1

    # loop through each num in nums
    for num in nums:
        # for each num if the num is even multiply it with the total and store the result in the total
        if num % 2 == 0:
            total *= num

    # return total
    return total
