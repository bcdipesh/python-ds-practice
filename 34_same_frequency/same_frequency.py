def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    # create an empty dict called num1_count and num2_count
    num1_count = {}
    num2_count = {}

    # convert num1 and num2 to str and compare their length
    num1_str = str(num1)
    num2_str = str(num2)

    # if length of num1 and num2 is same proceed further
    if len(num1_str) == len(num2_str):
        # loop over characters of num1_str
        for i in range(0, len(num1_str)):
            # create an inner loop which starts at current index + 1
            for j in range(i + 1, len(num1_str)):
                # check if character at current index in outer loop matches with character with current index in inner loop
                if num1_str[i] == num1_str[j]:
                    # if it does create a key/value pair in num1_count where key is character at current index and value is the number of times it is matched
                    num1_count[num1_str[i]] = (
                        num1_count[num1_str[i]] + 1) if (num1_str[i] in num1_count) else 1

        # do the same process for num2_str
        for i in range(0, len(num2_str)):
            for j in range(i + 1, len(num2_str)):
                if num2_str[i] == num2_str[j]:
                    num2_count[num2_str[i]] = (
                        num2_count[num2_str[i]] + 1) if (num2_str[i] in num2_count) else 1

        # compare num1_count with num2_count and return the result
        return num1_count == num2_count
    # else return False
    else:
        return False
