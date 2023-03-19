def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    # make an empty dictionary
    count = {}

    # loop through each number in the nums
    for num in nums:
        # for each num check if the num is not present as a key in the dictionary
        if num not in count:
            # if this is the case create a key/value pair in dictionary where the key is the current num and the value is its total count in list
            count[num] = nums.count(num)

    # make a variable called most_common
    most_common = 0

    # loop through the dictionary keys and return the key that has the greatest value
    for num in count.keys():
        if most_common < count[num]:
            most_common = num

    return most_common
